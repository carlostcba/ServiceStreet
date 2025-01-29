import json
import pyodbc
import os
import shutil
from datetime import datetime

# Configurar la conexión a MSSQL
server = 'DESKTOP-NRBEVRF\\SQLEXPRESS'
database = 'ServiceStreet'
username = 'sa'
password = 'LaSalle2599'

conn_str = (
    f'DRIVER={{SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

# Función para convertir fechas
def convert_date(date_str):
    if date_str:
        try:
            return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return None
    return None

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
    priority INT,
    short_description NVARCHAR(MAX),
    description NVARCHAR(MAX),
    category NVARCHAR(100),
    subcategory NVARCHAR(100),
    urgency INT,
    impact INT,
    opened_at DATETIME NULL,
    resolved_at DATETIME NULL
)
'''
cursor.execute(create_table_sql)
conn.commit()

# Procesar todos los archivos JSON en la carpeta 'source'
source_dir = "Source"
processed_dir = "Processed"

if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

for filename in os.listdir(source_dir):
    if filename.endswith(".json"):
        file_path = os.path.join(source_dir, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        insert_sql = '''
        IF NOT EXISTS (SELECT 1 FROM incident_ga WHERE number = ?)
        INSERT INTO incident_ga (number, state, priority, short_description, description, category, subcategory, urgency, impact, opened_at, resolved_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''

        for record in data["records"]:
            cursor.execute(insert_sql, (
                record.get("number"),  # Para verificar si existe
                record.get("number"),
                record.get("state"),
                record.get("priority"),
                record.get("short_description"),
                record.get("description"),
                record.get("category"),
                record.get("subcategory"),
                record.get("urgency"),
                record.get("impact"),
                convert_date(record.get("opened_at")),
                convert_date(record.get("resolved_at"))
            ))

        conn.commit()
        
        # Renombrar y mover el archivo procesado
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_filename = f"processed_{timestamp}.json"
        shutil.move(file_path, os.path.join(processed_dir, new_filename))
        
        print(f"Archivo {filename} procesado y movido a {processed_dir} como {new_filename}")

# Cerrar conexión a la base de datos
cursor.close()
conn.close()

print("Todos los archivos han sido procesados exitosamente sin duplicar registros.")
