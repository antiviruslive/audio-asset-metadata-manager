import librosa
import numpy as np


class KeyAnalyzer:

    # Perfis de Krumhansl-Schmuckler para detecção de tonalidade
    MAJOR_PROFILE = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09,
                               2.52, 5.19, 2.39, 3.66, 2.29, 2.88])

    MINOR_PROFILE = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53,
                               2.54, 4.75, 3.98, 2.69, 3.34, 3.17])

    NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F',
                  'F#', 'G', 'G#', 'A', 'A#', 'B']

    def detect_key(self, file_path):

        try:

            y, sr = librosa.load(
                file_path,
                sr=None,
                mono=True
            )

            # Extrai o chromagram (energia por nota musical)
            chromagram = librosa.feature.chroma_cqt(y=y, sr=sr)
            chroma_mean = np.mean(chromagram, axis=1)

            # Correlaciona com os perfis maior e menor para cada nota raiz
            major_scores = []
            minor_scores = []

            for i in range(12):
                rotated = np.roll(chroma_mean, -i)
                major_scores.append(np.corrcoef(rotated, self.MAJOR_PROFILE)[0, 1])
                minor_scores.append(np.corrcoef(rotated, self.MINOR_PROFILE)[0, 1])

            best_major = np.argmax(major_scores)
            best_minor = np.argmax(minor_scores)

            if major_scores[best_major] >= minor_scores[best_minor]:
                return f"{self.NOTE_NAMES[best_major]} Major"
            else:
                return f"{self.NOTE_NAMES[best_minor]} Minor"

        except Exception as e:

            print(f"Erro ao detectar tonalidade: {e}")

            return None