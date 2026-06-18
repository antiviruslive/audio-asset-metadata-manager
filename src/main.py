import os

from readers.audio_reader import AudioReader
from analyzers.metadata_parser import MetadataParser

audio_folder = "audio_files"

reader = AudioReader()
parser = MetadataParser()

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

    print(normalized)