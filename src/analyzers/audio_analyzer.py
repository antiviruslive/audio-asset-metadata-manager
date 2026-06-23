class AudioAnalyzer:

    def get_duration(self, audio) -> float:

        try:
            return audio.info.length
        except:
            return 0.0

    def get_sample_rate(self, audio) -> int:

        try:
            return audio.info.sample_rate
        except:
            return 0

    def get_channels(self, audio) -> int:

        try:
            return audio.info.channels
        except:
            return 0