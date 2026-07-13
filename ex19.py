import pandas as pd
import numpy as np
def validate_data(df):
    """
    Retorna True si pasa las validaciones, False si falla o si faltan columnas requeridas.
    Validaciones:
    1. 'id' no debe tener nulos
    2. 'price' debe ser > 0
    """
    try:
        # Colocamos la lógica "riesgosa" dentro del try
        if df['id'].isna().any():
            return False
        elif (df['price'] <= 0).any():
            return False
        else:
            return True
            
    except KeyError:
        # Si Pandas no encuentra 'id' o 'price', saltará directamente aquí
        print("Error: El DataFrame no contiene las columnas requeridas ('id' o 'price').")
        return False
# Tests
df_ok = pd.DataFrame({'id': [1, 2], 'price': [10, 20]})
df_null = pd.DataFrame({'id': [1, np.nan], 'price': [10, 20]})
df_neg = pd.DataFrame({'id': [1, 2], 'price': [10, -5]})

# Test extra: DataFrame sin la columna 'price'
df_incomplete = pd.DataFrame({'id': [1, 2], 'sku': ['A', 'B']})

print(f"OK: {validate_data(df_ok)}")          # Retorna: True
print(f"Null Fail: {validate_data(df_null)}")  # Retorna: False
print(f"Neg Fail: {validate_data(df_neg)}")    # Retorna: False

print("\n--- Test de Columna Faltante ---")
print(f"Incomplete Fail: {validate_data(df_incomplete)}") # Imprime el mensaje y retorna: False