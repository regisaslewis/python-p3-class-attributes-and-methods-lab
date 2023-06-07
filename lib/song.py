class Song:
    count = 0
    all = []
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.all.append(self)
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        for n in cls.genres:
            cls.genre_count[genre] = 0
        for n in cls.all:
            if genre == n.genre:
                cls.genre_count[genre] += 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        for n in cls.artists:
            cls.artist_count[artist] = 0
        for n in cls.all:
            if artist == n.artist:
                cls.artist_count[artist] += 1