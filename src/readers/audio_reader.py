from mutagen import File


class AudioReader:

    def read(self, file_path: str):

        audio = File(file_path)

        if audio is None:
            return None

        return audio