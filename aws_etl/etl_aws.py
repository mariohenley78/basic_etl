import os
import sys
import pandas as pd
import awswrangler as wr
from dotenv import load_dotenv

# Cargar credenciales de AWS desde el archivo .env
load_dotenv()

# --- CONFIGURACION DE S3 ---
BUCKET_NAME = "amzn-myraw-bucket"  # Tu bucket de S3

S3_RAW_PREFIX = f"s3://{BUCKET_NAME}/raw/"
S3_PROCESSED_PREFIX = f"s3://{BUCKET_NAME}/processed/"


def extract(raw_prefix: str = S3_RAW_PREFIX) -> dict:
    """Extrae datos de los archivos CSV ubicados en la carpeta raw/ de S3."""
    print("EXTRACT: Cargando datos desde S3...")
    
    tables = {}
    csv_files = {
        'orders': 'ecommerce_orders.csv',
        'order_items': 'ecommerce_order_items.csv',
        'customers': 'ecommerce_customers.csv',
        'products': 'ecommerce_products.csv',
        'categories': 'ecommerce_categories.csv',
    }
    
    print(f"   Buscando {len(csv_files)} archivos en {raw_prefix}\n")
    
    for table_name, filename in csv_files.items():
        s3_path = f"{raw_prefix}{filename}"
        
        try:
            # Verificar si el archivo existe en S3
            if wr.s3.does_object_exist(s3_path):
                tables[table_name] = wr.s3.read_csv(path=s3_path)
                print(f"   [OK] {table_name}: {len(tables[table_name])} filas leidas")
            else:
                print(f"   [WARN] Archivo no encontrado: {filename}")
        except Exception as e:
            print(f"   [ERROR] Error al intentar acceder a {filename}: {e}")
    
    return tables


def transform(tables: dict) -> pd.DataFrame:
    """Limpia y transforma los datos."""
    print("\nTRANSFORM: Limpiando datos...")

    df = tables['orders'].copy()
    
    # 1. Manejar nulos
    antes = len(df)
    df = df.dropna(subset=['customer_id', 'total_amount'])
    print(f"   Filas eliminadas por nulos: {antes - len(df)}")
    
    # 2. Eliminar duplicados
    antes = len(df)
    df = df.drop_duplicates(subset=['order_id'], keep='last')
    print(f"   Duplicados eliminados: {antes - len(df)}")
    
    # 3. Corregir tipos
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total_amount'] = pd.to_numeric(df['total_amount'], errors='coerce')
    
    # 4. Agregar campos calculados
    df['order_month'] = df['order_date'].dt.to_period('M').astype(str)
    df['is_high_value'] = df['total_amount'] > 100
    
    print(f"   Filas finales a guardar: {len(df)}")
    return df


def load(df: pd.DataFrame, processed_prefix: str = S3_PROCESSED_PREFIX):
    """Guarda los resultados procesados directamente en la carpeta processed/ de S3."""
    print(f"\nLOAD: Guardando resultados en {processed_prefix}...")
    
    # 1. Guardar Dataset Principal Limpio (CSV y Parquet)
    wr.s3.to_csv(df=df, path=f'{processed_prefix}orders_clean.csv', index=False)
    wr.s3.to_parquet(df=df, path=f'{processed_prefix}orders_clean.parquet', index=False)
    print("   - Guardado: orders_clean.csv y orders_clean.parquet")
    
    # 2. Metricias: Ventas por Cliente
    ventas_cliente = df.groupby('customer_id')['total_amount'].sum().reset_index()
    wr.s3.to_csv(df=ventas_cliente, path=f'{processed_prefix}ventas_por_cliente.csv', index=False)
    print("   - Guardado: ventas_por_cliente.csv")
    
    # 3. Metricias: Ventas por Mes
    ventas_mes = df.groupby('order_month')['total_amount'].sum().reset_index()
    wr.s3.to_csv(df=ventas_mes, path=f'{processed_prefix}ventas_por_mes.csv', index=False)
    print("   - Guardado: ventas_por_mes.csv")
    
    print("   [OK] Todos los archivos fueron subidos a S3 exitosamente")


def main():
    print("=" * 50)
    print("ETL Pipeline S3 - E-commerce Data")
    print("=" * 50)
    
    tables = extract()
    
    # Control de errores si no existen las tablas requeridas
    if not tables or 'orders' not in tables or tables['orders'].empty:
        print("\n[STOP] PIPELINE DETENIDO: No se encontraron los archivos requeridos en la ruta RAW de S3.")
        print(f"   Asegurate de que los archivos esten subidos en '{S3_RAW_PREFIX}'.")
        return

    df_clean = transform(tables)
    load(df_clean)
    
    print("\nETL completado exitosamente en S3")


if __name__ == "__main__":
    main()
