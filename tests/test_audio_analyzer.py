from src.analyzers.audio_analyzer import AudioAnalyzer


class MockAudioInfo:

    def __init__(self):

        self.length = 120.5
        self.sample_rate = 44100
        self.channels = 2


class MockAudio:

    def __init__(self):

        self.info = MockAudioInfo()


def test_audio_analyzer():

    analyzer = AudioAnalyzer()

    audio = MockAudio()

    assert analyzer.get_duration(audio) == 120.5
    assert analyzer.get_sample_rate(audio) == 44100
    assert analyzer.get_channels(audio) == 2