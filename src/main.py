import os

from services.audio_asset_service import AudioAssetService
from exporters.json_exporter import JsonExporter
from exporters.csv_exporter import CsvExporter 
from analyzers.batch_analytics import BatchAnalytics
from exporters.analytics_exporter import AnalyticsExporter
from exporters.catalog_exporter import CatalogExporter  


audio_folder = "audio_files"

service = AudioAssetService()
exporter = JsonExporter()

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



exporter.export(
    audio_assets,
    "output/metadata.json"
)

csv_exporter = CsvExporter()
csv_exporter.export(audio_assets, "output/metadata.csv")

batch = BatchAnalytics()
analytics = batch.analyze(audio_assets)

analytics_exporter = AnalyticsExporter()
analytics_exporter.print_summary(analytics)
analytics_exporter.export(analytics, "output/analytics.json")

catalog_exporter = CatalogExporter()
catalog_exporter.export(audio_assets, analytics, "output/catalog.html")