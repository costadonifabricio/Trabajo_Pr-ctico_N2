# Descripción del Código

Este código se conecta a una base de datos MySQL y realiza varias operaciones relacionadas con la creación de tablas, importación de datos desde un archivo CSV y generación de archivos CSV.

## Funcionamiento

1. Conecta a la base de datos MySQL utilizando los parámetros de conexión proporcionados.
2. Verifica si la tabla "provincias" existe y la elimina en caso de que exista.
3. Crea la tabla "provincias" con los campos especificados.
4. Crea una carpeta llamada "provincias" si no existe.
5. Lee los datos del archivo CSV "localidades.csv".
6. Importa los datos del archivo CSV a la tabla "provincias" utilizando una sentencia SQL preparada.
7. Obtiene todas las provincias distintas de la tabla "provincias".
8. Para cada provincia, crea un archivo CSV en la carpeta "provincias" con el nombre de la provincia.
9. Escribe las localidades correspondientes a la provincia en el archivo CSV.
10. Escribe la cantidad de localidades al final del archivo CSV.

## Instalación

Para ejecutar este código, necesitarás tener instalado Python y la siguiente dependencia:

- MySQLdb: `pip install mysqlclient`

Además, asegúrate de tener un servidor MySQL en ejecución.

## NOTA

Este código está diseñado para trabajar con una base de datos MySQL y un archivo CSV específico.

