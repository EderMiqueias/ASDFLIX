from app import app
from flask import json, request
from app.model.DAO import GenreDAO
from app.model.VO.GenreVO import GenreVO


@app.route('/genres/')
def get_genres():
    genres = GenreDAO.get_all_genres()
    genres = json_format = json.dumps([genre.get_json() for genre in genres])
    return genres


@app.route('/genres/', methods=['POST'])
def new_genres():
    if request.form.get('nome') is not None and request.form.get('nome') is str:
        GenreDAO.new_genre(request.form.get('nome'))
        return {
            'status': 'Genero cadastrado com sucesso!'
        }
    return {
        'status': 'Error'
    }


@app.route('/genres/<int:id>/')
def get_genres_by_id(id):
    genre = GenreDAO.get_genres_by_id(id)
    if genre:
        return genre.get_json()
    return {
        'status': 'Genero inexistente!'
    }


@app.route('/genres/', methods=['PUT'])
def update_genres():
    id = request.form.get('id')
    nome = request.form.get('nome')
    if GenreDAO.get_genres_by_id(id):
        newGenre = GenreVO(id, nome)
        GenreDAO.update_genres(newGenre)
        return {
            'status': 'Genero atualizado!'
        }
    return {
        'status': 'Nao eh possivel atualizar um genero inexistente'
    }


@app.route('/genres/<int:id>/', methods=['DELETE'])
def delete_genres(id):
    if GenreDAO.get_genres_by_id(id):
        GenreDAO.delete_genres(id)
        return {
            'status': 'Genero deletado!'
        }
    return {
        'status': 'Error'
    }

