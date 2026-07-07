import pandas as pd

df = pd.DataFrame({
    'nombre': ['Ana', 'Bob', 'Carlos', 'Diana', 'Eva', 'Frank'],
    'dept': ['IT', 'Sales', 'IT', 'Sales', 'IT', 'Sales'],
    'salario': [5000, 4000, 5500, 4500, 4800, 5000]
})

# 1. Agregá columna 'salario_promedio_dept' con el promedio del departamento
# 2. Agregá columna 'diferencia' = salario - salario_promedio_dept

# Tu código aquí
df['salario_promedio_dept'] = df.groupby('dept')['salario'].transform('mean')
df['diferencia'] = df['salario'] - df['salario_promedio_dept']

print(df)