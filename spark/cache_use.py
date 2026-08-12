import time
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder \
    .appName("EjemploCache") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# 1. Simular un conjunto de datos
data = [(i, f"Usuario_{i % 50}", (i * 10) % 1000) for i in range(1, 200000)]
df_raw = spark.createDataFrame(data, ["id", "usuario", "monto"])

# 2. Transformaciones "pesadas" a nivel de fila
df_limpio = df_raw \
    .filter(F.col("monto") > 100) \
    .withColumn("iva", F.round(F.col("monto") * 0.16, 2)) \
    .withColumn("categoria", F.when(F.col("monto") > 500, "Premium").otherwise("Estandar"))

# ==============================================================================
# USO DE .cache()
# Le indicamos a Spark que guarde 'df_limpio' en la memoria RAM del clúster
# ==============================================================================
df_limpio.cache()


# --- PRIMERA ACCIÓN ---
# En esta primera acción, Spark ejecuta las transformaciones Y GUARDA los resultados en RAM.
inicio = time.time()
total_registros = df_limpio.count()
fin = time.time()
print(f"1ª Acción (count) - Tiempo consumido (Construye cache): {fin - inicio:.4f} segundos")
print(f"Total registros: {total_registros}")


# --- SEGUNDA ACCIÓN ---
# En la segunda acción, Spark LEE DIRECTAMENTE DE LA MEMORIA RAM. No recomputa el filtro ni el IVA.
inicio = time.time()
print("\n--- Vista previa de categoría Premium ---")
df_limpio.filter(F.col("categoria") == "Premium").show(5)
fin = time.time()
print(f"2ª Acción (show) - Tiempo consumido (Lee de cache): {fin - inicio:.4f} segundos")


# --- TERCERA ACCIÓN ---
# Nuevamente reutiliza la RAM.
inicio = time.time()
promedio_monto = df_limpio.select(F.avg("monto")).collect()[0][0]
fin = time.time()
print(f"\n3ª Acción (promedio) - Tiempo consumido (Lee de cache): {fin - inicio:.4f} segundos")


# ==============================================================================
# LIBERAR MEMORIA (Muy importante en producción)
# ==============================================================================
df_limpio.unpersist()

spark.stop()
