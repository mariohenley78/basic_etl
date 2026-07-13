def filter_extract(records: list[dict], 
                   condition, fields: list[str]) -> list[dict]:
    """
    Filtra registros y extrae campos específicos.
    
    Args:
        records: Lista de diccionarios
        condition: Función lambda para filtrar
        fields: Lista de campos a extraer
        
    Returns:
        Lista filtrada con solo los campos especificados
    """
    return [
        {field: record[field] for field in fields}
        for record in records
        if condition(record)
    ]