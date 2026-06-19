from analyzers.key_analyzer import KeyAnalyzer

analyzer = KeyAnalyzer()

key = analyzer.detect_key(
    "audio_files/2 GMS, Dickster & Legohead - Dala.wav"
)

print("KEY:", key)