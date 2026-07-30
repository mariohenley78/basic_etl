# 📊 Web Logs Analysis Pipeline

Un pipeline ETL (Extracción, Transformación y Carga) liviano e in-memory para procesar, limpiar y analizar logs de acceso e infraestructura en formato JSON utilizando **Python** y **DuckDB**.

---

## 🚀 Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Motor Analítico:** [DuckDB](https://duckdb.org/) (Consultas SQL analíticas de alto rendimiento en memoria)
* **Procesamiento de Datos:** Pandas, NumPy
* **Manejo de Rutas:** `pathlib` (Compatible con Windows, Mac y Linux)

---

## 📂 Estructura del Proyecto

```text
web_logs/
│
├── data/                         <-- Archivos JSON fuente (logs)
│   ├── logs_access_logs.json
│   └── logs_services.json
│
├── src/                          <-- Código fuente del pipeline
│   └── weblogs.py                <-- Script principal de ejecución
│
├── .gitignore                    <-- Archivos ignorados por Git
├── requirements.txt              <-- Dependencias de Python
└── README.md                     <-- Documentación del proyecto
