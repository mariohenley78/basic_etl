from pyspark.sql import SparkSession
from pyspark.sql import functions as F


spark = SparkSession.builder \
    .appName("agreggations") \
    .getOrCreate()

employees_data = (
    [
        (1, "Carlos", 101),
        (2, "Elena", 102),
        (3, "Mario", 101),
        (3, "Jose", 101),
        (3, "Juan", 101),
        (4, "Ana", 103),
        (5, "Roberto", 999)  # Departamento inexistente para probar el LEFT join
    ],
    ["emp_id", "emp_name", "dept_id"]
)


employees = spark.createDataFrame(employees_data[0], employees_data[1])
print("--- listado de empleados original ---")

employees.show()

print("--- listado de empleados sin duplicados ---")

employees = employees.dropDuplicates(["emp_id"])

employees.show()

spark.stop()
