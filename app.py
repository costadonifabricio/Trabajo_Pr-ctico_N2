import sys
import MySQLdb
import csv

# Ruta del archivo CSV
csv_file = 'C:/Users/fabri/Desktop/csv/localidades.csv'

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
    id INT AUTO_INCREMENT PRIMARY KEY,
    provincia VARCHAR(255),
    localidad VARCHAR(255),
    cp INT,
    id_prov_mstr INT
)
"""

# Definir la sentencia SQL para importar los datos del CSV
sql_import = f"""
LOAD DATA INFILE '{csv_file}'
INTO TABLE provincias
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\\n'
IGNORE 1 ROWS
(provincia, id, localidad, cp, id_prov_mstr)
"""

# Ejecutar la sentencia SQL para crear la tabla
try:
    cursor.execute(sql)
    print("Tabla creada con éxito")
except MySQLdb.Error as e:
    print("Error al crear la tabla:", e)

# Ejecutar la sentencia SQL para importar los datos del CSV
try:
    cursor.execute(sql_import)
    db.commit()
    print("Datos importados con éxito")
except MySQLdb.Error as e:
    print("Error al importar los datos:", e)

db.close()
