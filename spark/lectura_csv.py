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


# Detener la sesion
spark.stop()
