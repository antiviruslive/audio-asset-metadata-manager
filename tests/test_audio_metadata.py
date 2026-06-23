from src.models.audio_metadata import AudioMetadata


def test_audio_metadata_to_dict():

    asset = AudioMetadata(
        filename="test.wav",
        title="Test Song",
        artist="Test Artist",
        album="Test Album",
        genre="Psy-Trance",
        year="2025",
        track_number="1",
        duration=120.5,
        sample_rate=44100,
        channels=2,
        bpm=145.0,
        key="D# Minor"
    )

    data = asset.to_dict()

    assert data["filename"] == "test.wav"
    assert data["title"] == "Test Song"
    assert data["artist"] == "Test Artist"
    assert data["bpm"] == 145.0
    assert data["key"] == "D# Minor"