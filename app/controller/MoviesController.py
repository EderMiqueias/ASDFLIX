from app import app
from flask import request
from app.model.VO.MovieVO import MovieVO
from app.model.DAO import GenreDAO, ActorDAO, MovieDAO


@app.route('/movies/')
def get_movies():
    movies = MovieDAO.get_all_movies()
    movies = [movie.get_json() for movie in movies]
    return {
        'message': 'success',
        'response': movies
    }


@app.route('/movies/', methods=['POST'])
def new_movies():
    title = request.form.get('titulo')
    duration = (request.form.get('duracao'))
    id_genre = request.form.get('id_genero')
    imdb = request.form.get('imdb')
    actors = request.form.getlist('ator')
    validator = True

    if title and duration and id_genre and imdb and actors:
        if duration.isdigit() and id_genre.isdigit():
            if not GenreDAO.get_genres_by_id(id_genre):
                return {
                    'message': 'Genero inexistente'
                }, 400
            try:
                actors = [int(id_actor) for id_actor in actors]
            except ValueError:
                return {
                    'message': 'ID do ator deve ser inteiro'
                }, 400
            for id_actor in actors:
                if not ActorDAO.get_actors_by_id(id_actor):
                    return {
                       'message': f'Ator com ID: {id_actor} inexistente'
                    }, 400
            duration = int(request.form.get('duracao'))
            id_genre = int(request.form.get('id_genero'))
            try:
                imdb = float(imdb)
            except ValueError:
                validator = False
        else:
            validator = False

        if validator:
            MovieDAO.new_movie(title, duration, id_genre, imdb, actors)
            return {
                'message': 'Filme cadastrado com sucesso!'
            }, 201
    return {
        'message': 'Insira os dados corretamente!',
    }, 400


@app.route('/movies/<int:id>/')
def get_movies_by_id(id):
    movie = MovieDAO.get_movies_by_id(id)
    if movie:
        return {
            'message': 'Success!',
            'response': movie.get_json()
        }
    return {
        'message': 'Filme inexistente!',
        'response': {}
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
                    'message': 'Genero inexistente'
                }, 400
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
                'message': 'Filme atualizado com sucesso!'
            }
    return {
        'message': 'Nao foi possivel atualizar o filme'
    }, 400


@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movies(id):
    if MovieDAO.get_movies_by_id(id):
        MovieDAO.delete_movies(id)
        return {
            'message': 'Filme deletado!'
        }
    return {
        'message': 'Erro ao deletar o filme!'
    }


@app.route('/movies/imdb')
def get_movies_per_imdb():
    movies = MovieDAO.get_movies_per_imdb()
    movies = [movie.get_json() for movie in movies]
    return {
        'message': 'success',
        'response': movies
    }


@app.route('/movies/actor/<int:id_actor>/')
def get_movies_by_actor_id(id_actor):
    actor = ActorDAO.get_actors_by_id(id_actor)
    if not actor:
        return {
           'message': 'actor is not registered',
           'response': []
        }
    movies = MovieDAO.get_movies_by_actor_id(actor.id)
    if not movies:
        return {
           'message': 'There are no movies of this actor registered',
           'response': []
        }
    movies = [movie.get_json() for movie in movies]
    return {
        'message': 'success',
        'response': movies
    }


@app.route('/movies/genre/<int:id_genre>/')
def get_movies_by_genre_id(id_genre):
    genre = GenreDAO.get_genres_by_id(id_genre)
    if not genre:
        return {
            'message': 'genre is not registered',
            'response': []
        }
    movies = MovieDAO.get_movies_by_genre_id(genre.id)
    if not movies:
        return {
            'message': 'There are no movies of this genre registered',
            'response': []
        }
    movies = [movie.get_json() for movie in movies]
    print(movies)
    return {
        'message': 'success',
        'response': movies
    }
