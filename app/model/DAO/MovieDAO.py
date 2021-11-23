from app.model.VO.MovieVO import MovieVO
from app.util_db.conexao_bd import connect


def new_movie(title, duration, id_genre, imdb):
    cursor = connect.cursor()
    query = f"INSERT INTO movies (title, duration, id_genre, imdb) values ('{title}','{duration}','{id_genre}', '{imdb}')"
    cursor.execute(query)
    connect.commit()
    cursor.close()


def get_all_movies():
    cursor = connect.cursor()
    query = "SELECT * FROM movies"
    cursor.execute(query)
    movies = []
    data_manager = cursor.fetchone()
    while data_manager:
        movies.append(MovieVO(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4]))
        data_manager = cursor.fetchone()
    cursor.close()
    return movies


def get_movies_by_id(id):
    cursor = connect.cursor()
    query = f"SELECT * FROM movies where id={id}"
    cursor.execute(query)
    data_manager = cursor.fetchone()
    if data_manager:
        cursor.close()
        return MovieVO(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4])
    cursor.close()
    return None


def get_movies_by_id(id_actor):
    cursor = connect.cursor()
    query = f"SELECT * FROM movies where id={id_actor}"
    cursor.execute(query)
    data_manager = cursor.fetchone()
    if data_manager:
        cursor.close()
        return MovieVO(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4])
    cursor.close()


def update_movies(newMovie):
    cursor = connect.cursor()
    query = f"UPDATE movies SET title = '{newMovie.getTitle()}', duration='{newMovie.getDuration()}', id_genre='{newMovie.getIdGenre()}', imdb='{newMovie.getImdb()}' where id={newMovie.getId()}"
    cursor.execute(query)
    connect.commit()
    cursor.close()


def delete_movies(id):
    cursor = connect.cursor()
    query = f"DELETE FROM movies WHERE id={id}"
    cursor.execute(query)
    connect.commit()
    cursor.close()


def get_movies_per_imdb():
    cursor = connect.cursor()
    query = "select * from movies order by imdb desc"
    cursor.execute(query)
    movies = []
    data_manager = cursor.fetchone()
    while data_manager:
        movies.append(MovieVO(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4]))
        data_manager = cursor.fetchone()
    cursor.close()
    return movies


def get_movies_by_actor_id(id_actor):
    cursor = connect.cursor()
    query = f"""SELECT m.id, m.title, m.duration, m.id_genre, m.imdb FROM movies m
            LEFT JOIN movie_actor ma ON ma.id_movie = m.id WHERE ma.id_actor = {id_actor}"""
    cursor.execute(query)
    movies = []
    data_manager = cursor.fetchone()
    while data_manager:
        movies.append(MovieVO(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4]))
        data_manager = cursor.fetchone()
    cursor.close()
    return movies


def get_movies_by_genre_id(id_genre):
    cursor = connect.cursor()
    query = "SELECT * FROM movies" \
        f"WHERE movies.id_genre = {id_genre}"
    cursor.execute(query)
    movies = []
    data_manager = cursor.fetchone()
    while data_manager:
        movies.append(MovieVO(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4]))
        data_manager = cursor.fetchone()
    cursor.close()
    return movies

