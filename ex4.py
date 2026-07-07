def safe_divide(a, b):
    """Divide a/b de forma segura, retorna None si falla."""
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return None

# Tests
print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # None
print(safe_divide("a", 2))  # None
