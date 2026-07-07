import pandas as pd

productos = pd.DataFrame({
    'nombre': ['Laptop Pro', 'Mouse Basic', 'Monitor HD', 'Keyboard', 'Webcam'],
    'categoria': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories'],
    'precio': [999, 29, 349, 79, 89],
    'stock': [5, 100, 20, 50, 30]
})

# Usá query() para filtrar:
# - Productos de categoría 'Electronics'
# - Con precio menor a 500
# - Y stock mayor a 10

min_stock = 10
filtrados = None

filtrados = productos.query("categoria in ['Electronics'] and stock>@min_stock and precio < 500")

# Tu código aquí

print(filtrados)