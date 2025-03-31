import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        # Obtener la conexión utilizando las variables de entorno
        connection = psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE'),
            port=config('PGSQL_PORT')
        )
        # Mensaje para mostrar que la conexión se estableció correctamente
        print('Conexión exitosa!!')
        return connection
    except DatabaseError as ex:
        # Si ocurre un error, lo mostramos y lo regresamos
        print(f"Error al conectar con la base de datos: {ex}")
        return ex
