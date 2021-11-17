class GenreVO:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def get_json(self):
        return dict(
            id=self.id,
            nome=self.nome
        )

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome