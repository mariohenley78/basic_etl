------------------------------------------------------------------
-- 1. CREAR EL ROL
------------------------------------------------------------------


-- Crear un rol específico para esta tarea (Principio de menor privilegio)
CREATE ROLE IF NOT EXISTS MI_CARGADOR_ROLE;

-- Asignar el rol al usuario
GRANT ROLE MI_CARGADOR_ROLE TO USER SNOW_USER;


------------------------------------------------------------------
-- 2. ASIGNAR PERMISOS DE CÓMPUTO (WAREHOUSE)
------------------------------------------------------------------
-- Permitir al rol encender y ejecutar consultas con el Warehouse
GRANT USAGE ON WAREHOUSE MI_DWH_XS TO ROLE MI_CARGADOR_ROLE;


------------------------------------------------------------------
-- 3. ASIGNAR PERMISOS DE ESTRUCTURA (DATABASE Y SCHEMA)
------------------------------------------------------------------
-- Permitir ver/entrar a la Base de Datos y al Esquema
GRANT USAGE ON DATABASE MI_PROYECTO_DB TO ROLE MI_CARGADOR_ROLE;
GRANT USAGE ON SCHEMA MI_PROYECTO_DB.STAGING TO ROLE MI_CARGADOR_ROLE;


------------------------------------------------------------------
-- 4. ASIGNAR PERMISOS DE ACCIÓN (TABLAS Y STAGES PARA CSVs)
------------------------------------------------------------------
-- Permitir crear tablas dentro del esquema
GRANT CREATE TABLE ON SCHEMA MI_PROYECTO_DB.STAGING TO ROLE MI_CARGADOR_ROLE;

-- Permitir crear o usar Stages internos para subir los archivos CSV mediante PUT
GRANT CREATE STAGE ON SCHEMA MI_PROYECTO_DB.STAGING TO ROLE MI_CARGADOR_ROLE;

-- Permitir consultar, modificar e insertar datos en todas las tablas existentes y futuras
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA MI_PROYECTO_DB.STAGING TO ROLE MI_CARGADOR_ROLE;
GRANT SELECT, INSERT, UPDATE, DELETE ON FUTURE TABLES IN SCHEMA MI_PROYECTO_DB.STAGING TO ROLE MI_CARGADOR_ROLE;


GRANT CREATE FILE FORMAT ON SCHEMA MI_PROYECTO_DB.STAGING TO ROLE MI_CARGADOR_ROLE;
