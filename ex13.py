import pandas as pd

pedidos = pd.DataFrame({
    'pedido_id': [1, 2, 3, 4, 5],
    'fecha': ['2024-01-15', '2024-02-20', '2024-03-05', '2024-03-15', '2024-04-01']
})

# 1. Convertí 'fecha' a datetime
# 2. Extraé año, mes y día de la semana (nombre)
# 3. Calculá días desde el primer pedido

# Tu código aquí
pedidos['fecha'] = pd.to_datetime(pedidos['fecha'])
print (pedidos)
pedidos['año'] = pedidos['fecha'].dt.year
pedidos['mes'] = pedidos['fecha'].dt.month
pedidos['día_semana'] = pedidos['fecha'].dt.day_name()
fecha_min = pedidos['fecha'].min()
print (fecha_min)
pedidos['días_desde_primer_pedido'] = (pedidos['fecha'] - pedidos['fecha'].min()).dt.days

print(pedidos)