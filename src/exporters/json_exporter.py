import json


class JsonExporter:

    def export(self, audio_assets, output_file):

        data = []

        for asset in audio_assets:
            data.append(asset.to_dict())

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"\nJSON exported: {output_file}")