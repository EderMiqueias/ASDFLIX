class ActorVO:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_json(self):
        return dict(
            id=self.id,
            nome=self.name
        )

    def getId(self):
        return self.id

    def getName(self):
        return self.name

