from pyspark.sql import SparkSession
from pyspark.sql import functions as F


spark = SparkSession.builder \
    .appName("agreggations") \
    .getOrCreate()

data = [(1,"pasta",50,70),(2,"papel",20,10),(3,"escoba",10,15),(4,"jabon",15,3)]
schema = ["sales_id","Articulo","Cantidad","Precio"]

df =spark.createDataFrame (data,schema)


# Calculá el promedio por departamento
df = df \
     .withColumn("total", F.col("Cantidad") * F.col("Precio")) \
     .withColumn("categoria", F.when(F.col("Cantidad") > 10,"alto").otherwise("bajo"))

df = df.orderBy(F.col("total").asc())

df.show()
spark.stop()
