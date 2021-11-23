from app import app
from flask import request
from app.model.DAO import GenreDAO
from app.model.VO.GenreVO import GenreVO


@app.route('/genres/')
def get_genres():
    genres = GenreDAO.get_all_genres()
    genres = [genre.get_json() for genre in genres]
    return {
        'message': 'success',
        'response': genres
    }


@app.route('/genres/', methods=['POST'])
def new_genres():
    if request.form.get('nome') and request.form.get('nome').isdigit() is not True:
        GenreDAO.new_genre(request.form.get('nome'))
        return {
            'message': 'Genero cadastrado com sucesso!'
        }, 201
    return {
        'message': 'Digite os campos adequadamente'
    }, 400


@app.route('/genres/<int:id>/')
def get_genres_by_id(id):
    genre = GenreDAO.get_genres_by_id(id)
    if genre:
        return {
            'message': 'Success!',
            'response': genre.get_json()
        }
    return {
        'message': 'Genero inexistente!',
        'response': {}
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
                'message': 'Genero atualizado!'
            }
    return {
        'message': 'Nao foi possivel atualizar o genero'
    }, 400


@app.route('/genres/<int:id>/', methods=['DELETE'])
def delete_genres(id):
    if GenreDAO.get_genres_by_id(id):
        GenreDAO.delete_genres(id)
        return {
            'message': 'Genero deletado!'
        }
    return {
        'message': 'erro ao deletar o genero'
    }
