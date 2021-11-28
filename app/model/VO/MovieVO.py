class MovieVO:
    def __init__(self, id, title, duration, id_genre, imdb, actors):
        self.id = id
        self.title = title
        self.duration = duration
        self.id_genre = id_genre
        self.imdb = imdb
        self.actors = actors

    def get_json(self):
        return dict(
            id=self.id,
            title=self.title,
            duration=self.duration,
            id_genre=self.id_genre,
            imdb=self.imdb,
            actors=self.actors
        )

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title

    def getDuration(self):
        return self.duration

    def getIdGenre(self):
        return self.id_genre

    def getImdb(self):
        return self.imdb
    
    def getactors(self):
        return self.actors
