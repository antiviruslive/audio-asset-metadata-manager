import os

from models.audio_metadata import AudioMetadata
from readers.audio_reader import AudioReader
from analyzers.metadata_parser import MetadataParser
from analyzers.audio_analyzer import AudioAnalyzer
from exporters.json_exporter import JsonExporter

audio_folder = "audio_files"

reader = AudioReader()
parser = MetadataParser()
analyzer = AudioAnalyzer()
audio_assets = []

for file_name in os.listdir(audio_folder):

    file_path = os.path.join(audio_folder, file_name)

    if not os.path.isfile(file_path):
        continue

    print("\n" + "=" * 50)
    print(f"FILE: {file_name}")
    print("=" * 50)

    audio = reader.read(file_path)

    if audio is None:
        print("Unsupported file.")
        continue

    normalized = parser.parse_tags(audio.tags)

duration = analyzer.get_duration(audio)
sample_rate = analyzer.get_sample_rate(audio)
channels = analyzer.get_channels(audio)

track = AudioMetadata(
    filename=file_name,
    title=normalized.get("title"),
    artist=normalized.get("artist"),
    album=normalized.get("album"),
    genre=normalized.get("genre"),
    year=normalized.get("year"),
    track_number=normalized.get("track_number"),
    duration=duration,
    sample_rate=sample_rate,
    channels=channels
)

tracks.append(track)

print(track.to_dict())

exporter = JsonExporter()

exporter.export(
    tracks,
    "output/metadata.json"
)