class AudioMetadata:

    def __init__(
        self,
        filename,
        title,
        artist,
        album,
        genre,
        year,
        track_number,
        duration,
        sample_rate,
        channels,
        bpm=None,
        key=None
    ):

        self.filename = filename
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.year = year
        self.track_number = track_number
        self.duration = duration
        self.sample_rate = sample_rate
        self.channels = channels
        self.bpm = bpm
        self.key = key

    def to_dict(self):

        return {
            "filename": self.filename,
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
            "genre": self.genre,
            "year": self.year,
            "track_number": self.track_number,
            "duration": round(self.duration, 2),
            "sample_rate": self.sample_rate,
            "channels": self.channels,
            "bpm": self.bpm,
            "key": self.key
        }