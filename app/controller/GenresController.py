from app import app
from flask import request
from app.model.DAO import GenreDAO
from app.model.VO.GenreVO import GenreVO


@app.route('/genre/')
def get_genres():
    genres = GenreDAO.get_all_genres()
    genres = [genre.get_json() for genre in genres]
    return {
        'message': 'success',
        'response': genres
    }


@app.route('/genre/', methods=['POST'])
def new_genres():
    if request.form.get('name') and request.form.get('name').isdigit() is not True and not any(not c.isalnum() for c in request.form.get('name')):
        GenreDAO.new_genre(request.form.get('name'))
        return {
            'message': 'Genero cadastrado com sucesso!'
        }, 201
    return {
        'message': 'Digite os campos adequadamente'
    }, 400


# def __teste(string):
#     for char in string:
#         if 65 >= ord(char) <= 122:
#             return False
#     return True


@app.route('/genre/<int:id>/')
def get_genres_by_id(id):
    genre = GenreDAO.get_genres_by_id(id)
    if genre:
        return {
            'message': 'Success!',
            'response': genre.get_json()
        }
    return {
        'message': 'Genero inexistente!',
        'response': {} # ?
    }


@app.route('/genre/', methods=['PUT'])
def update_genres():
    id = request.form.get('id')
    name = request.form.get('name')

    if id and name:
        if id.isdigit() and GenreDAO.get_genres_by_id(id) and not any(not c.isalnum() for c in name):
            newGenre = GenreVO(id, name)
            GenreDAO.update_genres(newGenre)
            return {
                'message': 'Genero atualizado!'
            }
    return {
        'message': 'Nao foi possivel atualizar o genero'
    }, 400


@app.route('/genre/<int:id>/', methods=['DELETE'])
def delete_genres(id):
    if GenreDAO.get_genres_by_id(id):
        GenreDAO.delete_genres(id)
        return {
            'message': 'Genero deletado!'
        }
    return {
        'message': 'erro ao deletar o genero'
    }
