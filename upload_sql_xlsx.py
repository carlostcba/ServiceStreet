import pandas as pd
import pyodbc
import os
import shutil
from datetime import datetime

# Configurar la conexión a MSSQL
server = 'DESKTOP-NRBEVRF\\SQLEXPRESS'
database = 'ServiceStreet'
username = 'sa'
password = 'Passw0rd!'

conn_str = (
    f'DRIVER={{SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

# Función para convertir fechas
def convert_date(date_value):
    if pd.notna(date_value):
        if isinstance(date_value, str):
            try:
                return datetime.strptime(date_value, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                return None
        elif isinstance(date_value, datetime):
            return date_value
    return None

# Función para limpiar valores de texto
def clean_text(value):
    return str(value).strip() if pd.notna(value) else None

# Crear directorios si no existen
source_dir = "Source"
processed_dir = "Processed"
logs_dir = "Logs"

for directory in [source_dir, processed_dir, logs_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Crear un archivo de log único para esta ejecución
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")  # Timestamp con milisegundos
log_file_path = os.path.join(logs_dir, f"error_log_{timestamp}.txt")

# Asegurarse de que el archivo de log exista
try:
    open(log_file_path, "w").close()
except Exception as e:
    print(f"Error al crear el archivo de log: {e}")
    exit(1)

# Conectar a la base de datos
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
except Exception as e:
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.now()} - Error al conectar a la base de datos: {str(e)}\n")
    print(f"Error al conectar a la base de datos. Detalles en {log_file_path}")
    exit(1)

# Crear tabla si no existe
create_table_sql = '''
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='IncidentGa' AND xtype='U')
CREATE TABLE IncidentGa (
    incidentID INT IDENTITY(1,1) PRIMARY KEY,
    incidentNumber NVARCHAR(50) UNIQUE,
    state NVARCHAR(50),
    shortDescription NVARCHAR(MAX),
    description NVARCHAR(MAX),
    location NVARCHAR(100),
    openedAt DATETIME NULL,
    userEnd NVARCHAR(100),
    assignedTo NVARCHAR(100) NULL,
    assignmentDate DATETIME NULL,
    resolutionDate DATETIME NULL,
    assignmentGroup NVARCHAR(100) NULL
)
'''
cursor.execute(create_table_sql)
conn.commit()

# Procesar archivos en el directorio Source
for filename in os.listdir(source_dir):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(source_dir, filename)
        
        # Leer archivo XLSX
        try:
            df = pd.read_excel(file_path)
        except Exception as e:
            with open(log_file_path, "a", encoding="utf-8") as log_file:
                log_file.write(f"{datetime.now()} - Error al leer el archivo {filename}: {str(e)}\n")
            continue

        # Contadores para registros procesados
        inserted_count = 0
        duplicate_count = 0
        omitted_count = 0

        # Verificar si el registro ya existe en las tres tablas
        check_sql = '''
        SELECT COUNT(1)
        FROM (
            SELECT incidentNumber FROM IncidentGa
            UNION
            SELECT incidentNumber FROM IncidentOpen
            UNION
            SELECT incidentNumber FROM IncidentClosed
        ) AS Combined
        WHERE incidentNumber = ?
        '''

        # Inserción de registro
        insert_sql = '''
        INSERT INTO IncidentGa (incidentNumber, state, shortDescription, description, location, openedAt, userEnd, assignmentGroup)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        
        # Procesar cada fila del archivo
        for _, row in df.iterrows():
            assignment_group = clean_text(row.get("Grupo de asignación"))
            
            # Filtrar registros según el grupo de asignación
            if assignment_group not in ["STEC-NovatiumNemoQ", "STEC-Novatium-SUC"]:
                omitted_count += 1
                continue
            
            try:
                # Verificar si el registro ya existe en cualquiera de las tres tablas
                cursor.execute(check_sql, clean_text(row.get("Número")))
                exists = cursor.fetchone()[0]
                if exists:
                    duplicate_count += 1
                    continue

                # Insertar si no existe
                cursor.execute(insert_sql, (
                    clean_text(row.get("Número")),
                    clean_text(row.get("Estado")),
                    clean_text(row.get("Breve descripción")),
                    clean_text(row.get("Descripcion")),
                    clean_text(row.get("Ubicación")),
                    convert_date(row.get("Abierto")),
                    clean_text(row.get("Usuario final")),
                    assignment_group
                ))
                inserted_count += 1
            except Exception as e:
                omitted_count += 1
                with open(log_file_path, "a", encoding="utf-8") as log_file:
                    log_file.write(f"{datetime.now()} - Error en archivo {filename}, registro: {row.to_dict()} - {str(e)}\n")
                continue  # Ignorar este registro y continuar con el siguiente

        # Confirmar transacciones
        conn.commit()
        
        # Registrar resumen de inserciones, duplicados y omisiones en el log
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write(
                f"{datetime.now()} - Archivo {filename}: {inserted_count} registros insertados, {duplicate_count} registros duplicados, {omitted_count} registros omitidos.\n"
            )
        
        # Mover siempre el archivo, incluso si hubo errores en algunos registros
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")  # Timestamp único
        new_filename = f"processed_incident_{timestamp}.xlsx"
        shutil.move(file_path, os.path.join(processed_dir, new_filename))
        
        print(f"Archivo {filename} procesado y movido a {processed_dir} como {new_filename}")

# Cerrar conexión a la base de datos
cursor.close()
conn.close()

print(f"Todos los archivos han sido procesados exitosamente. Logs guardados en: {log_file_path}")
