from database.db import get_connection
from .entities.Movie import Movie

class MovieModel():
    
   # METODO PARA TRAER TODOS LOS DATOS DE LA BASE DE DATOS
    
    @classmethod
    def get_movies(self):
        try:
            conection = get_connection()  # Asegúrate de que la función get_connection esté bien definida
            movies = []
            
            with conection.cursor() as cursor:
                cursor.execute('SELECT * FROM tb_usuarios')
                resultset = cursor.fetchall()
                
                for row in resultset:
                    movie = Movie(row[0],row[1], row[2], row[3])  # Suponiendo que row[1], row[2] y row[3] son atributos correctos
                    movies.append(movie.to_JSON())
            
            return movies  # Retorna la lista de películas

        except Exception as ex:
            raise Exception(ex)


# ESTOS SON METODOS ALTERNATIVOS
    # SI NO FUNCIONA EN LAS RUTAS EL LLAMAR EL OBJETO CON SUS ATRIBUTOS
    
# # Crear una instancia de MovieModel
# movie_model = MovieModel()

# # Obtener la lista de películas
# movies = movie_model.get_movies()

# METODO PARA BUSCAR SOLO UN USUARIO 
    @classmethod
    def get_movie(self, id_user):
        try:  
            conection = get_connection()  # Asegúrate de que la función get_connection esté bien definida
            
            with conection.cursor() as cursor:
                cursor.execute('SELECT * FROM tb_usuarios WHERE id_user = %s', (id_user,))
                row = cursor.fetchone()                
                
                movie = None
                if row != None:
                    movie = Movie(row[0],row[1], row[2], row[3])
                    movie = movie.to_JSON()
            
            conection.close()
            return movie  # Retorna la lista de películas
        except Exception as ex:
            raise Exception(ex)
        
# METODO PARA INGRESAR DATOS CON INSERT/INPUT
    @classmethod
    def add_movie(self, movie):
        try:  
            conection = get_connection()  # Asegúrate de que la función get_connection esté bien definida
            
            with conection.cursor() as cursor:
                cursor.execute("""INSERT INTO tb_usuarios (usuario, correo, contraseña) VALUES (%s, %s, %s)""", (movie.usuario, movie.correo, movie.contraseña))
            affected_rows = cursor.rowcount
            conection.commit()
            
            conection.close()
            return affected_rows  # Retorna la lista de películas
        except Exception as ex:
            raise Exception(ex)