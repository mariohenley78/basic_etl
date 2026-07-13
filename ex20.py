import json


def parse_jsonl(text: str) -> list[dict]:
    resultados = []
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        try:
            resultados.append(json.loads(line))
        except json.JSONDecodeError:
            # Aquí puedes usar la biblioteca logging para registrar la línea corrupta
            print(f"Advertencia: Saltando línea con JSON inválido: {line}")
            continue
    return resultados

# --- SECCIÓN DE PRUEBAS ---

def test_parse_jsonl_valid():
    """Caso Feliz: Datos perfectos y limpios."""
    jsonl_data = '{"id": 1, "name": "Laptop"}\n{"id": 2, "name": "Mouse"}'
    
    resultado = parse_jsonl(jsonl_data)
    
    assert len(resultado) == 2
    assert resultado[0]["name"] == "Laptop"
    assert resultado[1]["id"] == 2

def test_parse_jsonl_with_empty_lines():
    """Validar que ignore líneas vacías intermedias, iniciales o finales."""
    jsonl_data = '\n{"id": 1}\n   \n{"id": 2}\n'
    
    resultado = parse_jsonl(jsonl_data)
    
    assert len(resultado) == 2
    assert resultado[0]["id"] == 1
    assert resultado[1]["id"] == 2

def test_parse_jsonl_invalid_json():
    """Validar qué pasa si el JSON está mal formado."""
    jsonl_data = '{"id": 1}\n{"id": 2, "broken_json": }'
    
    # Aquí validamos que Python lance un JSONDecodeError debido a la línea rota
    with pytest.raises(json.JSONDecodeError):
        parse_jsonl(jsonl_data)

# Para ejecutar las pruebas si corres el archivo directamente con python test_parser.py
if __name__ == "__main__":
    print("Corriendo validaciones manuales...")
    test_parse_jsonl_valid()
    test_parse_jsonl_with_empty_lines()
    print("¡Todas las pruebas manuales pasaron con éxito!")