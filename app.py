import sys
import os
import MySQLdb
import csv

# Conectar a la base de datos
try:
    db = MySQLdb.connect("localhost", "root", "", "argentina")
except MySQLdb.Error as e:
    print("No puedo conectar a la base de datos:", e)
    sys.exit(1)

cursor = db.cursor()

# Verificar si la tabla existe y eliminarla
try:
    cursor.execute("DROP TABLE IF EXISTS provincias")
    print("Tabla eliminada exitosamente")
except MySQLdb.Error as e:
    print("Error al eliminar la tabla:", e)

# Definir la sentencia SQL para crear la tabla
sql = """
CREATE TABLE provincias (
    provincia VARCHAR(255),
    id VARCHAR(255),
    localidad VARCHAR(255),
    cp VARCHAR(255),
    id_prov_mstr VARCHAR(255)
)
"""

# Ejecutar la sentencia SQL para crear la tabla
try:
    cursor.execute(sql)
    print("Tabla creada con éxito")
except MySQLdb.Error as e:
    print("Error al crear la tabla:", e)

# Ruta de la carpeta para los archivos CSV
csv_folder = 'C:/Users/fabri/Desktop/csv/provincias'

# Crear la carpeta si no existe
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)
    print("Carpeta creada exitosamente")

# Ruta del archivo CSV
csv_file = 'C:/Users/fabri/Desktop/csv/localidades.csv'

# Definir la sentencia SQL para importar los datos del CSV
sql_import = f"""
LOAD DATA INFILE '{csv_file}'
INTO TABLE provincias
FIELDS TERMINATED BY ','
(provincia, id, localidad, cp, id_prov_mstr)
"""

# Ejecutar la sentencia SQL para importar los datos del CSV
try:
    cursor.execute(sql_import)
    db.commit()
    print("Datos importados con éxito")
except MySQLdb.Error as e:
    print("Error al importar los datos:", e)

# Obtener todas las provincias
cursor.execute("SELECT DISTINCT provincia FROM provincias")
provincias = cursor.fetchall()

for provincia in provincias:
    # Eliminar los caracteres no permitidos en el nombre de la provincia
    provincia_limpia = provincia[0].replace('"', '')

    # Obtener todas las localidades para la provincia actual
    cursor.execute(f"SELECT localidad FROM provincias WHERE provincia = '{provincia[0]}'")
    localidades = cursor.fetchall()

    # Crear un archivo CSV para la provincia actual en la carpeta de los CSV
    csv_path = os.path.join(csv_folder, f'{provincia_limpia}.csv')
    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
        writer.writerow(["Localidad"])

        # Escribir las localidades en el archivo CSV
        for localidad in localidades:
            writer.writerow([localidad[0]])

        # Escribir la cantidad de localidades al final del archivo CSV
        writer.writerow(["Cantidad de localidades", len(localidades)])

print("Archivos CSV generados con éxito")

db.close()
