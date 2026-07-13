import pandas as pd

data = {
    'id': [1, 2, 3],
    'updated_at': ['2023-01-10', '2023-01-12', '2023-01-05']
}
df = pd.DataFrame(data)

# Fecha de la última ejecución
last_run_date = '2023-01-08'

# Filtrá solo los registros posteriores a last_run_date
# (Convertí a datetime primero)
incremental_df = None
# Tu código aquí

last_run_date = pd.to_datetime(last_run_date)
df['updated_at'] = pd.to_datetime(data['updated_at'])
#print(df['updated_at'].dtype)
incremental_df = df[df['updated_at'] > last_run_date]


print(incremental_df)