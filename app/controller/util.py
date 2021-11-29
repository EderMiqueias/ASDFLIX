from app.model.DAO import ActorDAO


def actors_list_is_invalid(actors):
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
