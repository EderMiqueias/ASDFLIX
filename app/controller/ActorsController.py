from app import app
from flask import json, request
from app.model.DAO import ActorDAO
from app.model.VO.ActorVO import ActorVO


@app.route('/actors/')
def get_actors():
    actors = ActorDAO.get_all_actors()
    actors = json_format = json.dumps([actor.get_json() for actor in actors])
    return actors


@app.route('/actors/', methods=['POST'])
def new_actors():
    if request.form.get('nome') and request.form.get('nome').isdigit() is not True:
        ActorDAO.new_actor(request.form.get('nome'))
        return {
            'status': 'Ator cadastrado com sucesso!'
        }
    return {
        'status': 'Digite os campos adequadamente'
    }


@app.route('/actors/<int:id>/')
def get_actors_by_id(id):
    actor = ActorDAO.get_actors_by_id(id)
    if actor:
        return actor.get_json()
    return {
        'status': 'Genero inexistente!'
    }


@app.route('/actors/', methods=['PUT'])
def update_actors():
    id = request.form.get('id')
    name = request.form.get('nome')

    if id and name:
        if id.isdigit() and ActorDAO.get_actors_by_id(id) and (request.form.get('nome').isdigit() is not True):
            newActor = ActorVO(id, name)
            ActorDAO.update_actors(newActor)
            return {
                'status': 'Ator atualizado!'
            }
    return {
        'status': 'Nao foi possivel atualizar o ator'
    }


@app.route('/actors/<int:id>/', methods=['DELETE'])
def delete_actors(id):
    if ActorDAO.get_actors_by_id(id):
        ActorDAO.delete_actors(id)
        return {
            'status': 'Ator deletado!'
        }
    return {
        'status': 'Error'
    }
