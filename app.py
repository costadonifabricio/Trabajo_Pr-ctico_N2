import sys
import MySQLdb

## Conectar a la base de datos
try:
    db = MySQLdb.connect("localhost","root","","provincias" )
except MySQLdb.Error as e:
    print("No puedo conectar a la base de datos:",e)
    sys.exit(1)

cursor = db.cursor()

# Definir la sentencia SQL para crear la tabla
sql = """
CREATE TABLE localidades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    provincia VARCHAR(255),
    localidad VARCHAR(255),
    cp INT,
    id_prov_mstr INT
)
"""

## Ejecutar la sentencia SQL
try:
    cursor.execute(sql)
except MySQLdb.Error as e:
    print("Error al crear la tabla:", e)

db.close()