def deduplicate(records: list[dict], key: str) -> list[dict]:
    """
    Elimina registros duplicados por clave (Tu código original).
    """
    seen = set()
    result = []
    for record in records:
        key_value = record.get(key)
        if key_value not in seen:
            seen.add(key_value)
            result.append(record)
    return result


# ==========================================
# DATOS DE PRUEBA (DATASET DE CLIENTES)
# ==========================================
# Nota que el ID 101 y el ID 102 aparecen dos veces con datos distintos.
clientes_sucios = [
    {"id": 101, "nombre": "Ana", "version": 1},
    {"id": 102, "nombre": "Pedro", "version": 1},
    {"id": 101, "nombre": "Ana Gomez", "version": 2},  # Duplicado de ID 101
    {"id": 103, "nombre": "Carlos", "version": 1},
    {"id": 102, "nombre": "Pedro Silva", "version": 2}  # Duplicado de ID 102
]

print("--- EJECUTANDO PRUEBAS DE DEDUPLICACIÓN ---\n")

# ==========================================
# PRUEBA 1: Validar reducción de tamaño
# ==========================================
clientes_limpios = deduplicate(clientes_sucios, key="id")

print(f"Dataset original: {len(clientes_sucios)} registros.")
print(f"Dataset limpio:   {len(clientes_limpios)} registros.")
# Deberían quedar exactamente 3 registros (IDs: 101, 102, 103)
print(f"¿Se redujo correctamente?: {len(clientes_limpios) == 3}")
print("-" * 60)


# ==========================================
# PRUEBA 2: Validar la regla 'Mantiene el primero'
# ==========================================
# Para el ID 101, existía "Ana" (versión 1) y "Ana Gomez" (versión 2).
# Tu función promete mantener la primera ocurrencia. Verifiquemos:
primer_registro = clientes_limpios[0]

print("Verificando si mantuvo la primera ocurrencia:")
print(f"  Registro obtenido: {primer_registro}")
print(f"  ¿Es la versión 1?: {primer_registro['version'] == 1}")
print("-" * 60)


# ==========================================
# PRUEBA 3: ¿Qué pasa con una lista ya limpia?
# ==========================================
# Si le pasamos datos que no tienen duplicados, debería regresar exactamente lo mismo.
datos_limpios = [{"id": 1}, {"id": 2}]
resultado_limpio = deduplicate(datos_limpios, key="id")

print(f"Prueba con datos ya limpios:")
print(f"  ¿Mantiene la misma cantidad?: {len(resultado_limpio) == 2}")
print("-" * 60)


# ==========================================
# PRUEBA 4: ¿Qué pasa con una lista vacía?
# ==========================================
# Un caso de esquina vital: si no hay datos, no debe tronar el código.
resultado_vacio = deduplicate([], key="id")
print(f"Prueba con lista vacía:")
print(f"  ¿Resultado es una lista vacía?: {resultado_vacio == []}")
print("-" * 60)

# Impresión del resultado final estructurado
print("\nResultado Final del Dataset Deduplicado:")
import pprint
pprint.pprint(clientes_limpios)

print("-" * 60)

print(clientes_limpios)
