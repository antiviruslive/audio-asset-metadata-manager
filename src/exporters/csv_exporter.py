import csv


class CsvExporter:

    def export(self, audio_assets, output_file):

        if not audio_assets:
            print("Nenhum asset para exportar.")
            return

        data = [asset.to_dict() for asset in audio_assets]
        headers = list(data[0].keys())

        with open(output_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        print(f"\nCSV exported: {output_file}")