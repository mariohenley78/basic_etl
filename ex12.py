import pandas as pd

ventas = pd.DataFrame({
    'dia': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'],
    'ventas': [1000, 1500, 1200, 1800, 2000]
})

# 1. Calculá ventas_acumuladas (cumsum)
# 2. Calculá pct_acumulado (% acumulado del total)

# Tu código aquí
ventas['ventas_acumuladas'] = ventas['ventas'].cumsum() 
ventas['porcentaje_total']= ventas['ventas'].cumsum()  / ventas['ventas'].sum() * 100

#ventas['ventas_acumuladas'] = ventas['ventas'].cumsum()
#ventas['pct_acumulado'] = ventas['ventas'].cumsum() / ventas['ventas'].sum() * 100

print(ventas)