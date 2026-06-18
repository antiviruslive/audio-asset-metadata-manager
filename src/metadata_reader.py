from mutagen import File
import os

audio_folder = "audio_files"

for file_name in os.listdir(audio_folder):

    file_path = os.path.join(audio_folder, file_name)

    if os.path.isfile(file_path):

        print("\n")
        print("=" * 60)
        print(f"FILE: {file_name}")
        print("=" * 60)

        audio = File(file_path)

        if audio is None:

            print("Formato não suportado.")
            continue

        print("\nINFORMAÇÕES TÉCNICAS")

        try:
            print("Length:", audio.info.length)
        except:
            pass

        try:
            print("Sample Rate:", audio.info.sample_rate)
        except:
            pass

        try:
            print("Channels:", audio.info.channels)
        except:
            pass

        print("\nMETADADOS")

        if audio.tags:

            for key, value in audio.tags.items():
                print(f"{key}: {value}")

        else:
            print("Nenhum metadado encontrado.")