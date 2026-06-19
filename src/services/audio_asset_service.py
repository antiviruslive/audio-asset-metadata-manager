from readers.audio_reader import AudioReader
from analyzers.metadata_parser import MetadataParser
from analyzers.audio_analyzer import AudioAnalyzer
from analyzers.bpm_analyzer import BPMAnalyzer
from models.audio_metadata import AudioMetadata


class AudioAssetService:

    def __init__(self):

        self.reader = AudioReader()
        self.parser = MetadataParser()
        self.analyzer = AudioAnalyzer()
        self.bpm_analyzer = BPMAnalyzer()

    def process_file(self, file_path, file_name):

        audio = self.reader.read(file_path)

        if audio is None:
            return None

        normalized = self.parser.parse_tags(audio.tags)

        duration = self.analyzer.get_duration(audio)
        sample_rate = self.analyzer.get_sample_rate(audio)
        channels = self.analyzer.get_channels(audio)
        bpm = self.bpm_analyzer.detect_bpm(file_path)

        asset = AudioMetadata(
            filename=file_name,
            title=normalized.get("title"),
            artist=normalized.get("artist"),
            album=normalized.get("album"),
            genre=normalized.get("genre"),
            year=normalized.get("year"),
            track_number=normalized.get("track_number"),
            duration=duration,
            sample_rate=sample_rate,
            channels=channels,
            bpm=bpm
        )

        return asset