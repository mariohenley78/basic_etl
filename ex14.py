import pandas as pd

ventas = pd.DataFrame({
    'categoria': ['Electro', 'Ropa', 'Electro', 'Ropa', 'Electro', 'Ropa'],
    'producto': ['TV', 'Camisa', 'Laptop', 'Pantalón', 'Phone', 'Vestido'],
    'monto': [500, 50, 1000, 80, 800, 120],
    'cantidad': [2, 10, 1, 15, 3, 8]
})

# Calculá por categoría:
# - total_ventas: suma de monto
# - promedio_monto: promedio de monto
# - productos_vendidos: count de producto
# - max_cantidad: máximo de cantidad

resumen = None

# Tu código aquí
resumen = ventas.groupby('categoria').agg(
    total_ventas=('monto', 'sum'),
    promedio_monto=('monto', 'mean'),
    productos_vendidos=('producto', 'count'),
    max_cantidad=('cantidad', 'max')
).reset_index()


print(resumen)