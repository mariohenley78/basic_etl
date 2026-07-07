#
productos = [
    {'nombre': 'Laptop', 'precio': 999},
    {'nombre': 'Mouse', 'precio': 29},
    {'nombre': 'Monitor', 'precio': 299}
]

# Ordená por precio ascendente
ordenados = sorted(productos, key=lambda x: x['precio'])
print(ordenados)
