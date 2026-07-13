def process_with_errors(records: list[dict], transform_fn) -> tuple[list, list]:
    """
    Procesa registros capturando errores individuales.
    
    Args:
        records: Lista de registros a procesar
        transform_fn: Función de transformación
        
    Returns:
        Tupla (resultados_exitosos, lista_de_errores)
        Cada error tiene: index, record, error, type
    """
    successful = []
    errors = []
    
    for index, record in enumerate(records):
        try:
            transformed = transform_fn(record)
            successful.append(transformed)
        except Exception as e:
            errors.append({
                "index": index,
                "record": record,
                "error": str(e),
                "type": type(e).__name__
            })
    
    return successful, errors
