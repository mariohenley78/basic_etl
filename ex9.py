import pandas as pd

data = {'price': [20, 60, 45, 80, 10]}
df = pd.DataFrame(data)

# Creá columna 'category': 'High' si price > 50, sino 'Low'
# Tu código aquí

def categoria(x):
    if x > 50: return 'High'
    else: return 'Low'

df['Category']=df['price'].apply(categoria)

print(df)