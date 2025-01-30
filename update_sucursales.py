import pandas as pd
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

# Conectar a la base de datos
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Crear tabla si no existe
create_table_sql = '''
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='sucursales_ga' AND xtype='U')
CREATE TABLE sucursales_ga (
    id INT IDENTITY(1,1) PRIMARY KEY,
    Location NVARCHAR(100),
    N° NVARCHAR(10),
    Nombre NVARCHAR(100),
    Dirección NVARCHAR(255),
    Localidad NVARCHAR(100),
    C_P NVARCHAR(10),
    Provincia NVARCHAR(100),
    Geolocalizacion NVARCHAR(255)
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
        IF NOT EXISTS (SELECT 1 FROM sucursales_ga WHERE N° = ?)
        INSERT INTO sucursales_ga (Location, N°, Nombre, Dirección, Localidad, C_P, Provincia, Geolocalizacion)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        
        for _, row in df.iterrows():
            cursor.execute(insert_sql, (
                row.get("N°"),  # Para verificar si existe
                row.get("Location"),
                row.get("N°"),
                row.get("Nombre"),
                row.get("Dirección"),
                row.get("Localidad"),
                row.get("C.P."),
                row.get("Provincia"),
                row.get("Geolocalizacion")
            ))

        conn.commit()
        
        # Renombrar y mover el archivo procesado
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_filename = f"processed_{timestamp}.xlsx"
        shutil.move(file_path, os.path.join(processed_dir, new_filename))
        
        print(f"Archivo {filename} procesado y movido a {processed_dir} como {new_filename}")

# Cerrar conexión a la base de datos
cursor.close()
conn.close()

print("Todos los archivos han sido procesados exitosamente sin duplicar registros.")
