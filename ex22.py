def batch_generator(items: list, batch_size: int):
    """
    Generador que divide items en batches.
    
    Args:
        items: Lista de elementos
        batch_size: Tamaño de cada batch
        
    Yields:
        Listas de tamaño batch_size (o menos para el último)
    """
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

