from app import app
from flask import request
from app.model.VO.MovieVO import MovieVO
from app.model.DAO import GenreDAO, ActorDAO, MovieDAO


@app.route('/movie/')
def get_movies():
    movies = MovieDAO.get_all_movies()
    movies = [movie.get_json() for movie in movies]
    return {
        'message': 'success',
        'response': movies
    }


@app.route('/movie/', methods=['POST'])
def new_movies():
    title = request.form.get('title')
    duration = (request.form.get('duration'))
    id_genre = request.form.get('id_genre')
    imdb = request.form.get('imdb')
    actors = request.form.getlist('actor')
    validator = True

    if title and duration and id_genre and imdb and actors:
        if duration.isdigit() and id_genre.isdigit():
            if not GenreDAO.get_genres_by_id(id_genre):
                return {
                    'message': 'genre inexistente'
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
            duration = int(request.form.get('duration'))
            id_genre = int(request.form.get('id_genre'))
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


@app.route('/movie/<int:id>/')
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


@app.route('/movie/', methods=['PUT'])
def update_movies():
    id = request.form.get('id')
    title = request.form.get('title')
    duration = (request.form.get('duration'))
    id_genre = request.form.get('id_genre')
    imdb = request.form.get('imdb')
    actors = request.form.getlist('actor')
    validator = True

    if title and duration and id_genre and imdb and id:
        if duration.isdigit() and id_genre.isdigit() and id.isdigit() and MovieDAO.get_movies_by_id(id):
            if not GenreDAO.get_genres_by_id(id_genre):
                return {
                    'message': 'genre inexistente'
                }, 400
            duration = int(request.form.get('duration'))
            id_genre = int(request.form.get('id_genre'))
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


@app.route('/movie/<int:id>', methods=['DELETE'])
def delete_movies(id): # deletar tb de movie actor
    if MovieDAO.get_movies_by_id(id):
        MovieDAO.delete_movies(id)
        return {
            'message': 'Filme deletado!'
        }
    return {
        'message': 'Erro ao deletar o filme!'
    }


@app.route('/movie/imdb')
def get_movies_per_imdb():
    movies = MovieDAO.get_movies_per_imdb()
    movies = [movie.get_json() for movie in movies]
    return {
        'message': 'success',
        'response': movies
    }


@app.route('/movie/actor/<int:id_actor>/')
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


@app.route('/movie/genre/<int:id_genre>/')
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
    return {
        'message': 'success',
        'response': movies
    }
