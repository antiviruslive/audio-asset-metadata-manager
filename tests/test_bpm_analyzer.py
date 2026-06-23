from unittest.mock import patch
import numpy as np

from src.analyzers.bpm_analyzer import BPMAnalyzer


@patch("src.analyzers.bpm_analyzer.librosa.beat.beat_track")
@patch("src.analyzers.bpm_analyzer.librosa.load")
def test_detect_bpm(mock_load, mock_beat_track):

    mock_load.return_value = (
        np.array([0.1, 0.2, 0.3]),
        44100
    )

    mock_beat_track.return_value = (
        np.array([145.0]),
        None
    )

    analyzer = BPMAnalyzer()

    bpm = analyzer.detect_bpm("fake_file.wav")

    assert bpm == 145.0