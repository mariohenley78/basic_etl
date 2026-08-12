from pyspark.sql import SparkSession
from pyspark.sql import functions as F


spark = SparkSession.builder \
    .appName("agreggations") \
    .getOrCreate()

data = [("Sistemas","Juan",50),("Sistemas","Maria",20),("Marketing","Pedro",10),("Marketing","Jose",15)]
schema = ["Departamento","Nombre","Salario"]

df =spark.createDataFrame (data,schema)


# Calculá el promedio por departamento
result = df.groupby("Departamento").agg(F.avg("Salario").alias("promedio_salario"))
result.show()

spark.stop()

