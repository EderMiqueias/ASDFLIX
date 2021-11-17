class MovieVO:
    def __init__(self, id, title, duration, id_genre, imdb):
        self.id = id
        self.title = title
        self.duration = duration
        self.id_genre = id_genre
        self.imdb = imdb

    def get_json(self):
        return dict(
            id=self.id,
            title=self.title,
            duration=self.duration,
            id_genre=self.id_genre,
            imdb=self.imdb
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
