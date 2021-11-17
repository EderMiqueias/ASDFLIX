from app.util_db.conexao_bd import connect


def createTableGenre():
    cursor = connect.cursor()
    table = 'CREATE TABLE IF NOT EXISTS genres (id serial primary key, name varchar(45))'
    cursor.execute(table)
    connect.commit()
    cursor.close()


createTableGenre()


def createTableActor():
    cursor = connect.cursor()
    table = 'CREATE TABLE IF NOT EXISTS actors (id serial primary key, name varchar(45))'
    cursor.execute(table)
    connect.commit()
    cursor.close()


createTableActor()


def createTableMovie():
    cursor = connect.cursor()
    table = 'CREATE TABLE IF NOT EXISTS movies (id serial primary key, ' \
            'title varchar(100),' \
            'duration integer,' \
            'id_genre integer,' \
            'imdb float)'
    cursor.execute(table)
    connect.commit()
    cursor.close()


createTableMovie()