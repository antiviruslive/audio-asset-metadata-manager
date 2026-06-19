import librosa
import numpy as np


class BPMAnalyzer:

    def detect_bpm(self, file_path):

        try:

            y, sr = librosa.load(
                file_path,
                sr=None,
                mono=True
            )

            tempo, _ = librosa.beat.beat_track(
                y=y,
                sr=sr
            )

            if isinstance(tempo, np.ndarray):
                tempo = tempo[0]

            return round(float(tempo), 2)

        except Exception as e:

            print(f"Erro ao detectar BPM: {e}")

            return None