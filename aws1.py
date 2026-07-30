import os
import io
import boto3
import pandas as pd
from dotenv import load_dotenv


load_dotenv()

s3_client = boto3.client('s3')

BUCKET_NAME = 'amzn-myraw-bucket'  # Reemplaza con el nombre de tu bucket
FILE_KEY = 'raw/clientes/marketing_data.csv'  # Reemplaza con la ruta del archivo

try:

	# 1. Obtener el objeto de S3
	response = s3_client.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)

	# 2. Convertir el Stream de bytes a texto y cargarlo en Pandas
	csv_content = response['Body'].read().decode('utf-8')
	df = pd.read_csv(io.StringIO(csv_content))

	# 3. Explorar los datos
	print("✅ DataFrame cargado exitosamente!")
	print(f"Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas\n")
	print(df.head())
except Exception as e:
    print(f"❌ Error al leer el archivo: {e}")
