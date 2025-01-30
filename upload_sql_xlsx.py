import pandas as pd
import pyodbc
import os
import shutil
from datetime import datetime

# Configurar la conexión a MSSQL
server = 'DESKTOP-NRBEVRF\SQLEXPRESS'
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

# Conectar a la base de datos
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Crear tabla si no existe
create_table_sql = '''
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='incident_ga' AND xtype='U')
CREATE TABLE incident_ga (
    id INT IDENTITY(1,1) PRIMARY KEY,
    number NVARCHAR(50) UNIQUE,
    state NVARCHAR(50),
    short_description NVARCHAR(MAX),
    description NVARCHAR(MAX),
    location NVARCHAR(100),
    opened_at DATETIME NULL,
    user_end NVARCHAR(100),
    assigned_to NVARCHAR(100) NULL,
    assignment_date DATETIME NULL,
    resolution_date DATETIME NULL,
    assignment_group NVARCHAR(100) NULL
)
'''
cursor.execute(create_table_sql)
conn.commit()

# Directorios
source_dir = "Source"
processed_dir = "Processed"

if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

for filename in os.listdir(source_dir):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(source_dir, filename)
        
        # Leer archivo XLSX
        df = pd.read_excel(file_path)
        
        insert_sql = '''
        IF NOT EXISTS (SELECT 1 FROM incident_ga WHERE number = ?)
        INSERT INTO incident_ga (number, state, short_description, description, location, opened_at, user_end, assignment_group)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        
        for _, row in df.iterrows():
            assignment_group = clean_text(row.get("Grupo de asignación"))
            
            # Filtrar registros según el grupo de asignación
            if assignment_group not in ["STEC-NovatiumNemoQ", "STEC-Novatium-SUC"]:
                continue
            
            cursor.execute(insert_sql, (
                clean_text(row.get("Número")),  # Para verificar si existe
                clean_text(row.get("Número")),
                clean_text(row.get("Estado")),
                clean_text(row.get("Breve descripción")),
                clean_text(row.get("Descripcion")),
                clean_text(row.get("Ubicación")),
                convert_date(row.get("Abierto")),
                clean_text(row.get("Usuario final")),
                assignment_group
            ))

        conn.commit()
        
        # Renombrar y mover el archivo procesado
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_filename = f"processed_incident_{timestamp}.xlsx"
        shutil.move(file_path, os.path.join(processed_dir, new_filename))
        
        print(f"Archivo {filename} procesado y movido a {processed_dir} como {new_filename}")

# Cerrar conexión a la base de datos
cursor.close()
conn.close()

print("Todos los archivos han sido procesados exitosamente sin duplicar registros.")
