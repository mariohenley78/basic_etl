from collections import defaultdict

def aggregate_by(records: list[dict], group_key: str, agg_key: str) -> dict:
    """
    Agrupa registros y calcula sum, count y avg (Tu función original).
    """
    groups = defaultdict(list)
    for r in records:
        if group_key in r and agg_key in r:
            groups[r[group_key]].append(r[agg_key])
    return {
        key: {
            'sum': sum(values),
            'count': len(values),
            'avg': sum(values) / len(values)
        }
        for key, values in groups.items()
    }


# ==============================================================================
# 1. DATASET DE PRUEBA (HISTORIAL DE VENTAS)
# ==============================================================================
# Tenemos 3 ventas de "Electrónica", 2 de "Ropa" y 1 de "Libros"
ventas_del_dia = [
    {"id": 1, "categoria": "Electrónica", "monto": 1200.00},
    {"id": 2, "categoria": "Ropa",        "monto": 350.00},
    {"id": 3, "categoria": "Electrónica", "monto": 800.00},
    {"id": 4, "categoria": "Ropa",        "monto": 450.00},
    {"id": 5, "categoria": "Libros",      "monto": 250.00},
    {"id": 6, "categoria": "Electrónica", "monto": 1000.00}
]

# ==============================================================================
# 2. EJECUCIÓN DE LA FUNCIÓN
# ==============================================================================
# Queremos agrupar por la columna "categoria" y resumir la columna "monto"
reporte_categorias = aggregate_by(
    records=ventas_del_dia, 
    group_key="categoria", 
    agg_key="monto"
)

# ==============================================================================
# 3. IMPRESIÓN DEL REPORTE FINAL
# ==============================================================================
print("--- REPORTE DE METRICAS POR CATEGORÍA ---")
from pprint import pprint
pprint(reporte_categorias)
