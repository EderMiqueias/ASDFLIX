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
    if request.form.get('nome') and request.form.get('nome').isdigit() is not True:
        GenreDAO.new_genre(request.form.get('nome'))
        return {
            'status': 'Genero cadastrado com sucesso!'
        }
    else:
        return {
            'status': 'Digite os campos adequadamente'
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
    name = request.form.get('nome')

    if id and name:
        if id.isdigit() and GenreDAO.get_genres_by_id(id) and request.form.get('nome').isdigit() is not True:
            newGenre = GenreVO(id, name)
            GenreDAO.update_genres(newGenre)
            return {
                'status': 'Genero atualizado!'
            }
    return {
        'status': 'Nao foi possivel atualizar o genero'
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

