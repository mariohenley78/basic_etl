import os
import json
import pandas as pd
from pyspark.sql import SparkSession

# 1. Crear la sesión de Spark
spark = SparkSession.builder \
    .appName("LecturaFormatos") \
    .getOrCreate()

# Desactivar logs innecesarios para mantener limpia la consola
spark.sparkContext.setLogLevel("ERROR")


# --- PASO PREVIO: GENERAR ARCHIVOS DE PRUEBA LOCALES ---
os.makedirs("datos_demo", exist_ok=True)

# Dataset 1: CSV (E-commerce)
df_csv = pd.DataFrame({
    "order_id": [101, 102, 103],
    "customer": ["Ana", "Carlos", "Elena"],
    "amount": [150.5, 99.0, 300.2]
})
df_csv.to_csv("datos_demo/ordenes.csv", index=False)

# Dataset 2: Parquet (Transacciones de Banco)
df_parquet = pd.DataFrame({
    "tx_id": ["TX-1", "TX-2", "TX-3"],
    "account_id": [5541, 8821, 5541],
    "balance": [1200.0, 4500.5, 980.0]
})
df_parquet.to_parquet("datos_demo/transacciones.parquet", index=False)

# Dataset 3: JSON (Eventos de Aplicacion / Logs)
data_json = [
    {"event_id": "E10", "event_name": "login", "user_id": 12},
    {"event_id": "E11", "event_name": "click_button", "user_id": 45},
    {"event_id": "E12", "event_name": "logout", "user_id": 12}
]
with open("datos_demo/eventos.json", "w") as f:
    for record in data_json:
        f.write(json.dumps(record) + "\n")

print("Archivos de prueba generados en la carpeta datos_demo/\n")


# ==============================================================================
# 1. LECTURA DE ARCHIVO CSV
# ==============================================================================
print("=== 1. LECTURA CSV ===")
# header=True para tomar la primera fila como nombres de columna
# inferSchema=True para que Spark detecte automaticamente tipos (int, float, etc.)
df_spark_csv = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("datos_demo/ordenes.csv")

df_spark_csv.show()
df_spark_csv.printSchema()


# ==============================================================================
# 2. LECTURA DE ARCHIVO PARQUET
# ==============================================================================
print("=== 2. LECTURA PARQUET ===")
# Parquet almacena el esquema y los tipos de datos de forma nativa dentro del archivo.
# No es necesario usar header ni inferSchema.
df_spark_parquet = spark.read.format("parquet") \
    .load("datos_demo/transacciones.parquet")

df_spark_parquet.show()
df_spark_parquet.printSchema()


# ==============================================================================
# 3. LECTURA DE ARCHIVO JSON
# ==============================================================================
print("=== 3. LECTURA JSON ===")
# Spark lee archivos JSON donde cada linea contiene un objeto JSON completo (JSON Lines / NDJSON).
df_spark_json = spark.read.format("json") \
    .load("datos_demo/eventos.json")

df_spark_json.show()
df_spark_json.printSchema()


# Detener la sesion
spark.stop()
