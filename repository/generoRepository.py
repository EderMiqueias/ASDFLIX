import connection_db


class GeneroRepository:
    def __init__(self, connection_class=connection_db.PostgreConnectionDb) -> None:
        self.connection = connection_class()
        pass

    def get_generos(self):
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute("select * from genero")
            resposta = cursor.fetchall()

        return resposta
