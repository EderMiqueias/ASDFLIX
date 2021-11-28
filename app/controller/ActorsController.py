from app import app
from flask import request
from app.model.DAO import ActorDAO
from app.model.VO.ActorVO import ActorVO


@app.route('/actor/')
def get_actors():
    actors = ActorDAO.get_all_actors()
    actors = [actor.get_json() for actor in actors]
    return {
        'message': 'success',
        'response': actors
    }


@app.route('/actor/', methods=['POST'])
def new_actors():
    if request.form.get('name') and not request.form.get('name').isdigit():
        ActorDAO.new_actor(request.form.get('name'))
        return {
            'message': 'Ator cadastrado com sucesso!'
        }, 201
    return {
        'message': 'Digite os campos adequadamente'
    }, 400


@app.route('/actor/<int:id>/')
def get_actors_by_id(id):
    actor = ActorDAO.get_actors_by_id(id)
    if actor:
        return {
            'message': 'Success!',
            'response': actor.get_json()}
    return {
        'message': 'Ator inexistente!',
        'response': {}
    }


@app.route('/actor/', methods=['PUT'])
def update_actors():
    id = request.form.get('id')
    name = request.form.get('name')

    if id and name:
        if id.isdigit() and ActorDAO.get_actors_by_id(id) and (request.form.get('name').isdigit() is not True):
            newActor = ActorVO(id, name)
            ActorDAO.update_actors(newActor)
            return {
                'message': 'Ator atualizado!'
            }
    return {
        'message': 'Nao foi possivel atualizar o ator'
    }, 400


@app.route('/actor/<int:id>/', methods=['DELETE'])
def delete_actors(id):
    if ActorDAO.get_actors_by_id(id):
        ActorDAO.delete_actors(id)
        return {
            'message': 'Ator deletado!'
        }
    return {
        'message': 'Error'
    }
