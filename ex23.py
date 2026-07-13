def transform_fields(record: dict, mapping: dict) -> dict:
    """
    Renombra campos de un diccionario.
    
    Args:
        record: Diccionario original
        mapping: Dict con old_name -> new_name
        
    Returns:
        Diccionario con campos renombrados
    """
    return {mapping.get(k, k): v for k, v in record.items()}
