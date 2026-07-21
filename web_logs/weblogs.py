import duckdb
import pandas
import numpy

# Conectar a DuckDB (en memoria - los datos se pierden al cerrar)
# Si querés persistir: con = duckdb.connect('mis_logs.db')
con = duckdb.connect()

# DuckDB puede leer JSON directamente (esto es genial!)
con.execute("""
    CREATE TABLE logs AS 
    SELECT * FROM read_json_auto('data/logs_access_logs.json')
""")

# Verificar que cargó bien
print("=" * 60)
print("Total de filas:", con.execute("SELECT COUNT(*) FROM logs").fetchone()[0])
print("=" * 60)

# Ver estructura de la tabla (igual que en PostgreSQL)
print("=" * 60)
print("\nColumnas:")
for col in con.execute("DESCRIBE logs").fetchall():
    print(f"  {col[0]}: {col[1]}")
print("=" * 60)

# Ver primeras filas
print("=" * 60)
print("\nPrimeras 3 filas:")
print(con.execute("SELECT * FROM logs LIMIT 3").fetchdf())
print("=" * 60)

#exploracion de datos
exploracion = """SELECT 
    COUNT(*) as total_requests,
    MIN(timestamp) as primera_request,
    MAX(timestamp) as ultima_request,
    COUNT(DISTINCT user_id) as usuarios_unicos,
    COUNT(DISTINCT endpoint) as endpoints_unicos
FROM logs;
"""
print("=" * 60)
print("1. DATOS GENERALES") 
print("=" * 60)
print(con.execute(exploracion).fetchdf())
#top endpoints


top_endpoints = """SELECT 
    endpoint,
    COUNT(*) as hits,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM logs), 2) as porcentaje
FROM logs
GROUP BY endpoint
ORDER BY hits DESC
LIMIT 10;
"""
print("=" * 60)
print("2. TOP 10 ENDPOINTS MÁS VISITADOS")
print("=" * 60)
print(con.execute(top_endpoints).fetchdf())

top_error_endpoint= """
SELECT 
    endpoint,
    COUNT(*) as total_errors,
    COUNT(DISTINCT user_id) as usuarios_afectados,
    ROUND(AVG(response_time_ms), 2) as avg_response_time
FROM logs
WHERE status_code >= 500
GROUP BY endpoint
ORDER BY total_errors DESC
LIMIT 10;
"""
print("=" * 60)
print("3. TOP ENDPOINTS CON MÁS ERRORES 500")
print("=" * 60)
print(con.execute(top_error_endpoint).fetchdf())

print("=" * 60)
print("4. PERFORMANCE POR ENDPOINT")
print("=" * 60)

performance = """
SELECT 
    endpoint,
    COUNT(*) as requests,
    ROUND(AVG(response_time_ms), 2) as avg_time,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY response_time_ms), 2) as p50,
    ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY response_time_ms), 2) as p95,
    MAX(response_time_ms) as max_time
FROM logs
WHERE status_code < 500  -- Solo requests exitosas
GROUP BY endpoint
HAVING COUNT(*) > 10  -- Solo endpoints con suficiente tráfico
ORDER BY p95 DESC
LIMIT 10;
"""

print(con.execute(performance).fetchdf())

tendencia = """
SELECT 
    EXTRACT(HOUR FROM timestamp) as hora,
    COUNT(*) as requests,
    ROUND(AVG(response_time_ms), 2) as avg_response_time,
    SUM(CASE WHEN status_code >= 500 THEN 1 ELSE 0 END) as errors
FROM logs
GROUP BY EXTRACT(HOUR FROM timestamp)
ORDER BY hora;
"""

print("=" * 60)   
print("5. TENDENCIA POR HORA")
print("=" * 60)

print(con.execute(tendencia).fetchdf())


top_lentos = """
WITH ranked AS (
    SELECT 
        endpoint,
        timestamp,
        response_time_ms,
        user_id,
        ROW_NUMBER() OVER (
            PARTITION BY endpoint 
            ORDER BY response_time_ms DESC
        ) as rank
    FROM logs
    WHERE status_code < 500
)
SELECT * FROM ranked 
WHERE rank <= 3
ORDER BY endpoint, rank;
"""

print("=" * 60)
print("6. TOP 3 REQUESTS MÁS LENTOS POR ENDPOINT")
print("=" * 60)

print(con.execute(top_lentos).fetchdf())


comparativa = """
WITH dailystats AS (
    SELECT 
        DATE(timestamp) as fecha,
        COUNT(*) as requests,
        ROUND(AVG(response_time_ms), 2) as avg_time
    FROM logs
    GROUP BY DATE(timestamp)
)
SELECT 
    fecha,
    requests,
    LAG(requests) OVER (ORDER BY fecha) as requests_dia_anterior,
    requests - LAG(requests) OVER (ORDER BY fecha) as diferencia,
    ROUND(
        (requests - LAG(requests) OVER (ORDER BY fecha)) * 100.0 / 
        LAG(requests) OVER (ORDER BY fecha), 
        2
    ) as cambio_porcentual
FROM dailystats
ORDER BY fecha;
"""

print("=" * 60)
print("7. COMPARATIVA DE TRAFICO POR DIA")
print("=" * 60)  

print(con.execute(comparativa).fetchdf())
