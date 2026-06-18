from mutagen import File


class AudioReader:

    def read(self, file_path):

        audio = File(file_path)

        if audio is None:
            return None

        return audio