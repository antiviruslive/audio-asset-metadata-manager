from collections import Counter


class BatchAnalytics:

    def analyze(self, audio_assets):

        if not audio_assets:
            return None

        data = [asset.to_dict() for asset in audio_assets]

        bpms = [d["bpm"] for d in data if d["bpm"] is not None]
        durations = [d["duration"] for d in data if d["duration"] is not None]
        keys = [d["key"] for d in data if d["key"] is not None]
        genres = list({d["genre"] for d in data if d["genre"] is not None})

        most_common_key = Counter(keys).most_common(1)[0][0] if keys else None

        analytics = {
            "total_files": len(data),
            "bpm_average": round(sum(bpms) / len(bpms), 2) if bpms else None,
            "bpm_highest": max(bpms) if bpms else None,
            "bpm_lowest": min(bpms) if bpms else None,
            "total_duration_minutes": round(sum(durations) / 60, 2) if durations else None,
            "most_common_key": most_common_key,
            "genres_found": genres
        }

        return analytics