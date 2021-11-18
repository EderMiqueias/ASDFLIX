from app.model.VO.ActorVO import ActorVO
from app.util_db.conexao_bd import connect


def new_actor(name: str):
    cursor = connect.cursor()
    query = f"INSERT INTO actors (name) values ('{name}')"
    cursor.execute(query)
    connect.commit()
    cursor.close()


def get_all_actors():
    cursor = connect.cursor()
    query = "SELECT * FROM actors"
    cursor.execute(query)
    actors = []
    data_manager = cursor.fetchone()
    while data_manager:
        actors.append(ActorVO(data_manager[0], data_manager[1]))
        data_manager = cursor.fetchone()
    cursor.close()
    return actors


def get_actors_by_id(id):
    cursor = connect.cursor()
    query = f"SELECT * FROM actors where id={id}"
    cursor.execute(query)
    data_manager = cursor.fetchone()
    if data_manager:
        cursor.close()
        return ActorVO(data_manager[0], data_manager[1])
    cursor.close()
    return None


def update_actors(newActor): # ta func apenas no navegador
    cursor = connect.cursor()
    query = f"UPDATE actors SET name = '{newActor.getName()}' where id={newActor.getId()}"
    cursor.execute(query)
    connect.commit()
    cursor.close()


def delete_actors(id):
    cursor = connect.cursor()
    query = f"DELETE FROM actors WHERE id={id}"
    cursor.execute(query)
    connect.commit()
    cursor.close()
