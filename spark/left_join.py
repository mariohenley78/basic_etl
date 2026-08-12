# employees y departments son DataFrames
# Unilos por "dept_id" usando left join

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


spark = SparkSession.builder \
    .appName("agreggations") \
    .getOrCreate()


# 2. Definicion de las tuplas de listas (Datos + Nombres de Columnas)
employees_data = (
    [
        (1, "Carlos", 101),
        (2, "Elena", 102),
        (3, "Mario", 101),
        (4, "Ana", 103),
        (5, "Roberto", 999)  # Departamento inexistente para probar el LEFT join
    ],
    ["emp_id", "emp_name", "dept_id"]
)

departments_data = (
    [
        (101, "Ingenieria"),
        (102, "Finanzas"),
        (103, "Recursos Humanos"),
        (104, "Marketing")  # Departamento sin empleados
    ],
    ["dept_id", "dept_name"]
)

employees = spark.createDataFrame(employees_data[0], employees_data[1])
departments = spark.createDataFrame(departments_data[0], departments_data[1])


result = employees.join(departments,on="dept_id",how="left")
result.show()

spark.stop()
