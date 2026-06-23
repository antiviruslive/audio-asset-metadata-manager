from unittest.mock import patch
import numpy as np

from src.analyzers.key_analyzer import KeyAnalyzer


@patch("src.analyzers.key_analyzer.librosa.feature.chroma_cqt")
@patch("src.analyzers.key_analyzer.librosa.load")
def test_detect_key(mock_load, mock_chroma):

    mock_load.return_value = (
        np.array([0.1, 0.2, 0.3]),
        44100
    )

    mock_chroma.return_value = np.ones((12, 100))

    analyzer = KeyAnalyzer()

    result = analyzer.detect_key("fake.wav")

    assert result is not None
    assert isinstance(result, str)