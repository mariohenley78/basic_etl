#Creá una función que haga un LEFT JOIN entre dos listas de diccionarios usando una clave común.
def left_join(left: list[dict], right: list[dict], left_key: str, right_key: str) -> list[dict]:
    """
    Realiza un LEFT JOIN entre dos listas de diccionarios.
    
    Args:
        left: Lista de diccionarios del lado izquierdo
        right: Lista de diccionarios del lado derecho
        left_key: Clave en los diccionarios del lado izquierdo
        right_key: Clave en los diccionarios del lado derecho
        
    Returns:
        Lista de diccionarios resultante del LEFT JOIN
    """
    # Crear un diccionario para acceso rápido a los registros del lado derecho
    right_dict = {record[right_key]: record for record in right}
    
    result = []
    for left_record in left:
        # Obtener el valor de la clave en el registro izquierdo
        key_value = left_record.get(left_key)
        
        # Buscar el registro correspondiente en el lado derecho
        right_record = right_dict.get(key_value, {})
        
        # Combinar los registros (el registro derecho puede estar vacío)
        combined_record = {**left_record, **right_record}
        
        result.append(combined_record)
    
    return result

usuarios = [
    {"id_usuario": 1, "nombre": "Ana"},
    {"id_usuario": 2, "nombre": "Pedro"},  # Pedro no tiene suscripción
]

suscripciones = [
    {"id_sub": 1, "plan": "Premium", "precio": 99},
    {"id_sub": 3, "plan": "Basic", "precio": 49},
]

# Ejecutamos tu función conectando 'id_usuario' con 'id_sub'
resultado = left_join(
    left=usuarios, 
    right=suscripciones, 
    left_key="id_usuario", 
    right_key="id_sub"
)

from pprint import pprint
pprint(resultado)
