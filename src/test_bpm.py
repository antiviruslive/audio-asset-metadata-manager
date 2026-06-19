from analyzers.bpm_analyzer import BPMAnalyzer

analyzer = BPMAnalyzer()

bpm = analyzer.detect_bpm(
    "audio_files/2 GMS, Dickster & Legohead - Dala.wav"
)

print("BPM:", bpm)