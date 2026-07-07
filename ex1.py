import pandas as pd

data = {
    'name': ['Ana', 'Bob', 'Charlie', 'Diana', 'Frank'],
    'age': [28, 34, 22, 31, 40],
    'city': ['Madrid', 'London', 'NY', 'Paris', 'Rome']
}
df = pd.DataFrame(data)

# Filtrá personas mayores de 30
mayores_30 = None # Tu código aquí
mayores_30 = df[df['age'] > 30]

print(mayores_30)