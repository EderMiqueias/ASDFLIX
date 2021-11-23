import sys

from app import app
from flask import json, request
from app.model.VO.MovieVO import MovieVO
from app.model.DAO import GenreDAO, ActorDAO, MovieDAO


@app.route('/movies/')
def get_movies():
    movies = MovieDAO.get_all_movies()
    movies = json_format = json.dumps([movie.get_json() for movie in movies])
    return movies


@app.route('/movies/', methods=['POST'])
def new_movies():
    title = request.form.get('titulo')
    duration = (request.form.get('duracao'))
    id_genre = request.form.get('id_genero')
    imdb = request.form.get('imdb')
    validator = True

    if title and duration and id_genre and imdb:
        if duration.isdigit() and id_genre.isdigit():
            if not GenreDAO.get_genres_by_id(id_genre):
                return {
                    'status': 'Genero inexistente'
                }
            duration = int(request.form.get('duracao'))
            id_genre = int(request.form.get('id_genero'))
            try:
                imdb = float(imdb)
            except ValueError:
                validator = False
        else:
            validator = False

        if validator:
            MovieDAO.new_movie(title, duration, id_genre, imdb)
            return {
                'status': 'Filme cadastrado com sucesso!'
            }
    # retornar um 401
    return {
        'status': 'Insira os dados corretamente!'
    }


@app.route('/movies/<int:id>/')
def get_movies_by_id(id):
    movie = MovieDAO.get_movies_by_id(id)
    if movie:
        return movie.get_json()
    # retornar um 401?
    return {
        'status': 'Filme inexistente!'
    }


@app.route('/movies/', methods=['PUT'])
def update_movies():
    id = request.form.get('id')
    title = request.form.get('titulo')
    duration = (request.form.get('duracao'))
    id_genre = request.form.get('id_genero')
    imdb = request.form.get('imdb')
    validator = True

    if title and duration and id_genre and imdb and id:
        if duration.isdigit() and id_genre.isdigit() and id.isdigit() and MovieDAO.get_movies_by_id(id):
            if not GenreDAO.get_genres_by_id(id_genre):
                return {
                    'status': 'Genero inexistente'
                }
            duration = int(request.form.get('duracao'))
            id_genre = int(request.form.get('id_genero'))
            try:
                imdb = float(imdb)
            except ValueError:
                validator = False
        else:
            validator = False

        if validator:
            newMovie = MovieVO(id, title, duration, id_genre, imdb)
            MovieDAO.update_movies(newMovie)
            return {
                'status': 'Filme atualizado com sucesso!'
            }
    return {
        'status': 'Nao foi possivel atualizar o filme'
    }


@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movies(id):
    if MovieDAO.get_movies_by_id(id):
        MovieDAO.delete_movies(id)
        return {
            'status': 'Filme deletado!'
        }
    return {
        'status': 'Error'
    }


@app.route('/movies/imdb')
def get_movies_per_imdb():
    movies = MovieDAO.get_movies_per_imdb()
    movies = json.dumps([movie.get_json() for movie in movies])
    return movies


@app.route('/movies/actor/<int:id_actor>/')
def get_movies_by_actor_id(id_actor):
    actor = ActorDAO.get_actors_by_id(id_actor)
    if not actor:
        return {
            'error': 'actor is not registered'
        }, 400
    movies = MovieDAO.get_movies_by_actor_id(actor.id)
    movies = json.dumps([movie.get_json() for movie in movies])
    return movies


@app.route('/movies/genre/<int:id_genre>/')
def get_movies_by_genre_id(id_genre):
    genre = GenreDAO.get_genres_by_id(id_genre)
    if not genre:
        return {
            'error': 'genre is not registered'
        }, 400
    movies = MovieDAO.get_movies_by_genre_id(genre.id)
    movies = json.dumps([movie.get_json() for movie in movies])
    return movies
