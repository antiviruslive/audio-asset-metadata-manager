from analyzers.metadata_parser import MetadataParser

sample_tags = {
    "TIT2": "Deep Jungle Walk",
    "TPE1": "Astrix",
    "TALB": "He.Art",
    "TCON": "Psychedelic Trance",
    "TDRC": "2016"
}

parser = MetadataParser()

result = parser.parse_tags(sample_tags)

print(result)