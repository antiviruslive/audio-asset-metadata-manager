import json


class AnalyticsExporter:

    def export(self, analytics, output_file):

        if not analytics:
            print("Nenhum dado para exportar.")
            return

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(analytics, file, indent=4, ensure_ascii=False)

        print(f"\nAnalytics exported: {output_file}")

    def print_summary(self, analytics):

        if not analytics:
            return

        print("\n" + "=" * 42)
        print("           BATCH ANALYTICS")
        print("=" * 42)
        print(f"  Total de arquivos    : {analytics['total_files']}")
        print(f"  BPM médio            : {analytics['bpm_average']}")
        print(f"  BPM mais alto        : {analytics['bpm_highest']}")
        print(f"  BPM mais baixo       : {analytics['bpm_lowest']}")
        print(f"  Duração total        : {analytics['total_duration_minutes']} min")
        print(f"  Tonalidade comum     : {analytics['most_common_key']}")
        print(f"  Gêneros encontrados  : {', '.join(analytics['genres_found'])}")
        print("=" * 42)