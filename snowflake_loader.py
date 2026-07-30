import os
import sys
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER')
SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')

WAREHOUSE = 'MI_DWH_XS'
DATABASE = 'MI_PROYECTO_DB'
SCHEMA = 'STAGING'
ROLE = 'MI_CARGADOR_ROLE'

RUTA_CSV_LOCAL = '/Users/mariohenley/Python/data/ecommerce_products.csv'
NOMBRE_TABLA = 'products'
STAGE_TEMPORAL = 'STAGE_TEMP_CARGA'
FORMATO_CSV = 'FORMATO_CSV_INFER'


def validar_credenciales():
    if not all([SNOWFLAKE_USER, SNOWFLAKE_PASSWORD, SNOWFLAKE_ACCOUNT]):
        print("Error: Credenciales incompletas en variables de entorno.", file=sys.stderr)
        sys.exit(1)


def ejecutar_carga():
    validar_credenciales()

    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=WAREHOUSE,
        database=DATABASE,
        schema=SCHEMA,
        role=ROLE
    )

    cursor = conn.cursor()

    try:
        cursor.execute(f"""
            CREATE OR REPLACE FILE FORMAT {FORMATO_CSV}
                TYPE = 'CSV'
                PARSE_HEADER = TRUE
                FIELD_OPTIONALLY_ENCLOSED_BY = '"'
                ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE;
        """)

        cursor.execute(f"CREATE OR REPLACE STAGE {STAGE_TEMPORAL};")

        cursor.execute(f"PUT 'file://{RUTA_CSV_LOCAL}' @{STAGE_TEMPORAL} AUTO_COMPRESS=TRUE OVERWRITE=TRUE;")

        nombre_archivo_gzip = f"{os.path.basename(RUTA_CSV_LOCAL)}.gz"

        cursor.execute(f"""
            CREATE OR REPLACE TABLE {NOMBRE_TABLA}
            USING TEMPLATE (
                SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
                FROM TABLE(
                    INFER_SCHEMA(
                        LOCATION => '@{STAGE_TEMPORAL}/{nombre_archivo_gzip}',
                        FILE_FORMAT => '{FORMATO_CSV}'
                    )
                )
            );
        """)

        cursor.execute(f"""
            COPY INTO {NOMBRE_TABLA}
            FROM @{STAGE_TEMPORAL}/{nombre_archivo_gzip}
            FILE_FORMAT = (FORMAT_NAME = '{FORMATO_CSV}')
            MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;
        """)

        cursor.execute(f"SELECT COUNT(*) FROM {NOMBRE_TABLA};")
        total_registros = cursor.fetchone()[0]

        print(f"Carga finalizada correctamente. Registros insertados en {NOMBRE_TABLA}: {total_registros}")

    except Exception as e:
        print(f"Error durante el proceso de carga: {e}", file=sys.stderr)
        sys.exit(1)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    ejecutar_carga()
