import os

from services.audio_asset_service import AudioAssetService

audio_folder = "audio_files"

service = AudioAssetService()

audio_assets = []

for file_name in os.listdir(audio_folder):

    file_path = os.path.join(audio_folder, file_name)

    if not os.path.isfile(file_path):
        continue

    print("\n" + "=" * 50)
    print(f"FILE: {file_name}")
    print("=" * 50)

    asset = service.process_file(
        file_path,
        file_name
    )

    if asset is None:
        continue

    audio_assets.append(asset)

    print(asset.to_dict())