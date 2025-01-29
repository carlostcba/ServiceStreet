import json
import pyodbc
from datetime import datetime

# Configurar la conexión a MSSQL
server = 'DESKTOP-NRBEVRF\SQLEXPRESS'
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

# Cargar datos desde el archivo JSON
with open('source/incident.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

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
    number NVARCHAR(50),
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

# Insertar datos en la tabla
insert_sql = '''
INSERT INTO incident_ga (number, state, priority, short_description, description, category, subcategory, urgency, impact, opened_at, resolved_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

for record in data["records"]:
    cursor.execute(insert_sql, (
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

# Confirmar cambios y cerrar conexión
conn.commit()
cursor.close()
conn.close()

print("Datos importados exitosamente.")