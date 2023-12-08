class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the count of songs
        self.__class__.add_song_to_count()

        # Add genre to the genres list and update genre_count
        self.__class__.add_to_genres()

        # Add artist to the artists list and update artist_count
        self.__class__.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        if cls.genre_count.get(cls.genre) is None:
            cls.genre_count[cls.genre] = 1
            cls.genres.append(cls.genre)
        else:
            cls.genre_count[cls.genre] += 1

    @classmethod
    def add_to_artists(cls):
        if cls.artist_count.get(cls.artist) is None:
            cls.artist_count[cls.artist] = 1
            cls.artists.append(cls.artist)
        else:
            cls.artist_count[cls.artist] += 1

    @classmethod
    def add_to_genre_count(cls):
        genre_count = {}
        for genre in cls.genres:
            genre_count[genre] = cls.genre_count.get(genre, 0)
        return genre_count

    @classmethod
    def add_to_artist_count(cls):
        artist_count = {}
        for artist in cls.artists:
            artist_count[artist] = cls.artist_count.get(artist, 0)
        return artist_count
