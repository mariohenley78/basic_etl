import pandas as pd

data = {
    'date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'product': ['A', 'B', 'A', 'B'],
    'sales': [100, 200, 150, 250]
}
df = pd.DataFrame(data)

# Pivot table: fechas en filas, productos en columnas, suma de ventas
#pivot_df = None
pivot_df= df.pivot_table(index='date', columns='product', values='sales', aggfunc='sum')
print(pivot_df)