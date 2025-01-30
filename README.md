# README

## Descripción
Este script en Python procesa archivos Excel (.xlsx) y los inserta en una base de datos Microsoft SQL Server. Verifica si los registros ya existen antes de insertarlos y mueve los archivos procesados a una carpeta separada para evitar duplicaciones.

## Requisitos
- Python 3.x
- Microsoft SQL Server (SQL Server Express recomendado)
- Librerías de Python:
  - `pandas`
  - `pyodbc`

## Instalación
### 1. Instalación de Python
Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### 2. Instalación de dependencias
Ejecuta el siguiente comando para instalar las librerías necesarias:

```sh
pip install pandas pyodbc
```

### 3. Configuración de la Base de Datos
Este script está diseñado para conectarse a un servidor SQL Server Express con los siguientes parámetros:

- **Servidor:** `DESKTOP-NRBEVRF\SQLEXPRESS`
- **Base de datos:** `ServiceStreet`
- **Usuario:** `sa`
- **Contraseña:** `Passw0rd!`

Si necesitas cambiar estos valores, edita la siguiente sección en el código:

```python
server = 'DESKTOP-NRBEVRF\SQLEXPRESS'
database = 'ServiceStreet'
username = 'sa'
password = 'Passw0rd!'
```

También asegúrate de que SQL Server acepte autenticación con usuario y contraseña y que el usuario tenga permisos suficientes para crear y modificar tablas.

## Uso
1. Coloca los archivos `.xlsx` a procesar en la carpeta `Source`.
2. Ejecuta el script con:

```sh
python script.py
```

3. Los registros nuevos serán insertados en la tabla `incident_ga` de la base de datos.
4. Los archivos procesados se moverán automáticamente a la carpeta `Processed` con un nombre que incluye la fecha y hora de procesamiento.

## Estructura de la Tabla `incident_ga`
El script crea automáticamente la tabla `incident_ga` si no existe. La estructura es la siguiente:

| Campo              | Tipo de Dato       | Descripción |
|--------------------|-------------------|-------------|
| id                | INT (IDENTITY)     | Identificador único |
| number            | NVARCHAR(50)      | Número del incidente (único) |
| state             | NVARCHAR(50)      | Estado del incidente |
| short_description | NVARCHAR(MAX)     | Breve descripción |
| description       | NVARCHAR(MAX)     | Descripción detallada |
| location         | NVARCHAR(100)      | Ubicación |
| opened_at        | DATETIME           | Fecha de apertura |
| user_end         | NVARCHAR(100)      | Usuario final |
| assigned_to      | NVARCHAR(100) (NULL) | Usuario asignado |
| assignment_date  | DATETIME (NULL)    | Fecha de asignación |
| resolution_date  | DATETIME (NULL)    | Fecha de resolución |
| assignment_group | NVARCHAR(100) (NULL) | Grupo de asignación |

## Notas Adicionales
- Solo se insertarán registros cuyo "Grupo de asignación" sea `STEC-NovatiumNemoQ` o `STEC-Novatium-SUC`.
- Se eliminan los espacios en blanco innecesarios en los valores de texto.
- Se convierte la fecha de apertura al formato adecuado antes de la inserción.

## Autor
Carlos Facundo Tello
