from pyspark.sql import SparkSession

# 1. Crear o recuperar la sesión de Spark
spark = SparkSession.builder \
    .appName("MiPrimeraPrueba") \
    .getOrCreate()

# 2. Crear un conjunto de datos simple
datos = [("Ana", 28), ("Carlos", 35), ("Elena", 22)]
columnas = ["Nombre", "Edad"]

# 3. Convertirlo a un DataFrame de Spark
df = spark.createDataFrame(datos, columnas)

# 4. Mostrar el contenido
df.show()

# 5. Cerrar la sesión
spark.stop()
