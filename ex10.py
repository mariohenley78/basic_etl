import pandas as pd

productos = pd.DataFrame({
    'producto': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Webcam', 'Headset'],
    'precio': [999, 29, 349, 79, 89, 149],
    'stock': [10, 150, 45, 80, 30, 60]
})

# Encontrá los 3 productos más caros
top_3_caros = None
top_3_caros = productos.nlargest(3,'precio')
# Encontrá los 2 productos más baratos
top_2_baratos = None
top_2_baratos = productos.nsmallest(2,'precio')

print("Top 3 más caros:")
print(top_3_caros)
print("\nTop 2 más baratos:")
print(top_2_baratos)