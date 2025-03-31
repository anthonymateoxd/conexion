from flask import Blueprint,jsonify, request

#peticion get
from models.MovieModel import MovieModel

main=Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_movies():
    try:
        # movie_model = MovieModel()  # Crear una instancia de MovieModel 
        # movies = movie_model.get_movies()  # Llamar al método a través de la instancia
        movies= MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)})
        
@main.route('/<id_user>')
def get_movie(id_user):
    try:
        movie=MovieModel.get_movie(id_user)
        if movie!= None:
            return jsonify(movie)
        else:
            return jsonify({}),404
    except KeyError as ex:
        return ex
    
     
@main.route('/add', methods=['POST'])
def add_movie(): 
    try:
        print(request.json)
        usuario = request.json['usuario']
        email = request.json['email']
        contraña = request.json['contraseña']
        
        movie=Movie
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500