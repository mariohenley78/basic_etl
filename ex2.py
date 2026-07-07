import pandas as pd

data = {
    'department': ['IT', 'HR', 'IT', 'Sales', 'HR', 'IT'],
    'employee': ['A', 'B', 'C', 'D', 'E', 'F'],
    'salary': [5000, 4000, 5200, 6000, 4200, 5100]
}
df = pd.DataFrame(data)

# Calculá el salario promedio por departamento (df resultante debe tener 'department' y 'salary')
# Tip: usá reset_index() al final
avg_salary = df.groupby('department')['salary'].mean().reset_index()



print(avg_salary)
