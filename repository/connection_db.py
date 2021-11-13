import psycopg2


class PostgreConnectionDb:
    def __init__(self):
        self.server = 'localhost'
        self.port = 5432
        self.database = 'asd_flix'
        self.username = 'postgres'
        self.password = '1234'

    def __enter__(self):
        self.conn = psycopg2.connect(dbname=self.database, user=self.username,
                                     password=self.password, host=self.server, port=self.port)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
