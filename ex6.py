import pandas as pd

data = {
    'product': ['A', 'B', 'C'],
    'price': [10.0, 20.0, 15.0],
    'quantity': [5, 2, 10]
}
df = pd.DataFrame(data)

# Creá la columna 'total'
# Tu código aquí
df['total']=df['price'] * df['quantity']
print(df)
