import pandas as pd

usuarios = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'email': ['ana@test.com', 'bob@test.com', 'ana@test.com', 'carlos@test.com', 'bob@test.com'],
    'nombre': ['Ana', 'Bob', 'Ana García', 'Carlos', 'Robert'],
    'registro': ['2024-01-01', '2024-01-02', '2024-01-15', '2024-01-03', '2024-02-01']
})

print("Original:")
print(usuarios)

# 1. Contá cuántos emails duplicados hay
duplicados = 0

# 2. Eliminá duplicados por email, quedándote con el ÚLTIMO registro
usuarios_unicos = None

# Tu código aquí
duplicados = usuarios.duplicated(subset=['email']).sum()
usuarios_unicos = usuarios.drop_duplicates(subset=['email'], keep='last')
print(f"\nEmails duplicados: {duplicados}")
print("\nUsuarios únicos:")
print(usuarios_unicos)