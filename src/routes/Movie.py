from flask import Blueprint,jsonify, request
import uuid

#peticion get
from models.MovieModel import MovieModel

#Entities
from models.entities.Movie import Movie

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
    
        usuario = request.json['usuario']
        email = request.json['email']
        contraña = request.json['contraseña']
        id = uuid.uuid4()
        movie = movie = Movie(str(id),usuario, email, contraña)

        affect_rows = MovieModel.add_movie(movie)

        if affect_rows == 1:
            return jsonify(movie.id), 201
        else:
            return jsonify({'message': 'Error on insert'}), 500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_movie(id): 
    try:
    
        usuario = request.json['usuario']
        email = request.json['email']
        contraña = request.json['contraseña']
        id = uuid.uuid4()
        movie = movie = Movie(str(id),usuario, email, contraña)

        affect_rows = MovieModel.update_movie(movie)

        if affect_rows == 1:
            return jsonify(movie.id), 201
        else:
            return jsonify({'message': 'Error on insert'}), 500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500



@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id): 
    try:
        movie = Movie(id)
        affect_rows = MovieModel.delete_movie(movie)

        if affect_rows == 1:
            return jsonify(movie.id), 201
        else:
            return jsonify({'message': 'No movie delete'}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500