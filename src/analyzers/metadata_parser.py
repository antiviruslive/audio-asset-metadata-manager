class MetadataParser:

    TAG_MAPPING = {
        "TIT2": "title",
        "TPE1": "artist",
        "TALB": "album",
        "TCON": "genre",
        "TDRC": "year",
        "TRCK": "track_number"
    }

    def parse_tags(self, tags):

        normalized = {}

        if not tags:
            return normalized

        for key, value in tags.items():

            clean_key = str(key)

            if clean_key in self.TAG_MAPPING:

                normalized_key = self.TAG_MAPPING[clean_key]

                normalized[normalized_key] = str(value)

        return normalized