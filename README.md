# Audio Asset Metadata Manager

A professional Python application for extracting, analyzing, and organizing audio asset metadata.

This project was developed to process audio files, extract embedded metadata, analyze technical audio properties, detect BPM (tempo), and export structured data into JSON format for cataloging and asset management workflows.

---

## Features

### Metadata Extraction

Extracts metadata from audio files such as:

* Title
* Artist
* Album
* Genre
* Year
* Track Number

Supported through Mutagen metadata parsing.

---

### Technical Audio Analysis

Analyzes audio properties including:

* Duration
* Sample Rate
* Audio Channels

Useful for audio library management and quality control workflows.

---

### BPM Detection

Automatically detects the tempo (BPM) of audio files using Librosa.

Example:

```json
{
    "title": "Dala",
    "artist": "GMS & Dickster & Legohead",
    "bpm": 143.55
}
```

---

### JSON Export

Exports all collected information into a structured JSON file for:

* Asset cataloging
* Media management
* Data pipelines
* AI training datasets
* Audio library indexing

---

## Project Architecture

```text
audio-asset-metadata-manager
│
├── audio_files/
│
├── output/
│
├── src/
│   ├── analyzers/
│   │   ├── audio_analyzer.py
│   │   ├── bpm_analyzer.py
│   │   └── metadata_parser.py
│   │
│   ├── exporters/
│   │   └── json_exporter.py
│   │
│   ├── models/
│   │   └── audio_metadata.py
│   │
│   ├── readers/
│   │   └── audio_reader.py
│   │
│   ├── services/
│   │   └── audio_asset_service.py
│   │
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python 3
* Mutagen
* Librosa
* NumPy
* JSON

---

## Installation

Clone the repository:

```bash
git clone https://github.com/antiviruslive/audio-asset-metadata-manager.git
```

Navigate to the project directory:

```bash
cd audio-asset-metadata-manager
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Place audio files inside:

```text
audio_files/
```

Run the application:

```bash
python src/main.py
```

---

## Example Output

Console:

```text
==================================================
FILE: 2 GMS, Dickster & Legohead - Dala.wav
==================================================

{
    "filename": "2 GMS, Dickster & Legohead - Dala.wav",
    "title": "Dala",
    "artist": "GMS & Dickster & Legohead",
    "album": "Adverse Cambers",
    "genre": "Psy-Trance",
    "year": "2021",
    "track_number": "4",
    "duration": 368.54,
    "sample_rate": 44100,
    "channels": 2,
    "bpm": 143.55
}
```

Generated JSON:

```json
[
    {
        "filename": "2 GMS, Dickster & Legohead - Dala.wav",
        "title": "Dala",
        "artist": "GMS & Dickster & Legohead",
        "album": "Adverse Cambers",
        "genre": "Psy-Trance",
        "year": "2021",
        "track_number": "4",
        "duration": 368.54,
        "sample_rate": 44100,
        "channels": 2,
        "bpm": 143.55
    }
]
```

---

## Future Enhancements

Planned features:

* Musical Key Detection
* CSV Export
* Batch Analytics Dashboard
* Additional Audio Features Analysis
* Audio Fingerprinting
* Database Integration
* REST API Support

---

## Professional Skills Demonstrated

This project demonstrates:

* Object-Oriented Programming (OOP)
* Python Application Architecture
* Service Layer Pattern
* Metadata Processing
* Audio Signal Analysis
* JSON Data Export
* Git Version Control
* GitHub Project Management

---

## Author

Norton Henrique Silva

Audio Producer, DJ, Audio Technology Enthusiast and Software Engineering Student.

GitHub:
https://github.com/antiviruslive
