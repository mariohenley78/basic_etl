from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# 1. Iniciar la sesión de Spark
spark = SparkSession.builder \
    .appName("TransformacionesCSV") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# 2. Leer el CSV
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("datos_demo/ordenes.csv")

print("--- DATOS ORIGINALES DEL CSV ---")
df.show()

# ==============================================================================
# 1. .select() -> Seleccionar columnas específicas o renombrarlas
# ==============================================================================
# Útil para reducir el tamaño de los datos manteniendo solo las columnas de interés
df_seleccion = df.select("customer", "amount")

print("--- 1. RESULTADO DE .select() ---")
df_seleccion.show()


# ==============================================================================
# 2. .filter() -> Filtrar filas según una condición
# ==============================================================================
# Obtener solo las órdenes cuyo monto sea mayor a 100
df_filtrado = df.filter(F.col("amount") > 100)

print("--- 2. RESULTADO DE .filter() (amount > 100) ---")
df_filtrado.show()


# ==============================================================================
# 3. .withColumn() -> Crear nuevas columnas o modificar existentes
# ==============================================================================
# Agregar una columna con IVA (16%) y una columna condicional de cliente VIP
df_transformado = df \
    .withColumn("iva", F.round(F.col("amount") * 0.16, 2)) \
    .withColumn("total_con_iva", F.col("amount") + F.col("iva")) \
    .withColumn("es_vip", F.col("amount") >= 200)

print("--- 3. RESULTADO DE .withColumn() ---")
df_transformado.show()


# ==============================================================================
# ENCADENAMIENTO DE MÉTODOS (Method Chaining)
# En código de producción se suelen combinar todas en una sola instrucción
# ==============================================================================
df_final = df \
    .filter(F.col("amount") > 100) \
    .withColumn("impuesto", F.round(F.col("amount") * 0.16, 2)) \
    .select("order_id", "customer", "amount", "impuesto")

print("--- PIPELINE ENCADENADO COMPLETO ---")
df_final.show()

spark.stop()
