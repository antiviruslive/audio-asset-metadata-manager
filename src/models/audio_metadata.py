class AudioMetadata:

    def __init__(
        self,
        filename: str,
        title: str | None,
        artist: str | None,
        album: str | None,
        genre: str | None,
        year: str | None,
        track_number: str | None,
        duration: float,
        sample_rate: int,
        channels: int,
        bpm: float | None = None,
        key: str | None = None
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

    def to_dict(self) -> dict:

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