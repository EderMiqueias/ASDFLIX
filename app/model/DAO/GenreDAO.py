from app.model.VO.GenreVO import GenreVO
from app.util_db.conexao_bd import connect


def new_genre(name: str):
    cursor = connect.cursor()
    query = f"INSERT INTO genres (name) values ('{name}')"
    cursor.execute(query)
    connect.commit()
    cursor.close()


def get_all_genres():
    cursor = connect.cursor()
    query = "SELECT * FROM genres"
    cursor.execute(query)
    genres = []
    data_manager = cursor.fetchone()
    while data_manager:
        genres.append(GenreVO(data_manager[0], data_manager[1]))
        data_manager = cursor.fetchone()
    cursor.close()
    return genres


def get_genres_by_id(id):
    cursor = connect.cursor()
    query = f"SELECT * FROM genres where id={id}"
    cursor.execute(query)
    data_manager = cursor.fetchone()
    if data_manager:
        cursor.close()
        return GenreVO(data_manager[0], data_manager[1])
    cursor.close()
    return None


def update_genres(newGenre): # ta func apenas no navegador
    cursor = connect.cursor()
    query = f"UPDATE genres SET name = '{newGenre.getName()}' where id={newGenre.getId()}"
    cursor.execute(query)
    connect.commit()
    cursor.close()


def delete_genres(id):
    cursor = connect.cursor()
    query = f"DELETE FROM genres WHERE id={id}"
    cursor.execute(query)
    connect.commit()
    cursor.close()
