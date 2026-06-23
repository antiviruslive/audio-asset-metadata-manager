# Audio Asset Metadata Manager

A professional Python application for extracting, analyzing, and organizing audio asset metadata.

This project processes audio files, extracts embedded metadata, analyzes technical audio properties, detects BPM (tempo), identifies musical key signatures, generates analytics reports, and exports structured datasets in multiple formats.

Built with a modular architecture, automated testing, and continuous integration workflows.


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

---

### Musical Key Detection

Automatically detects the musical key of audio files using the Krumhansl-Schmuckler algorithm with chromagram analysis via Librosa.

---

### Batch Analytics

Generates a statistical summary of the entire audio catalog, including:

* Total files analyzed
* Average, highest and lowest BPM
* Total duration in minutes
* Most common musical key
* Genres found

Exported as `output/analytics.json` and displayed in the console.

---

### JSON Export

Exports all collected metadata into a structured JSON file for:

* Asset cataloging
* Media management
* Data pipelines
* AI training datasets
* Audio library indexing

---

### CSV Export

Exports all collected metadata into a CSV file for spreadsheet tools and data analysis workflows.

---

### HTML Asset Catalog

Generates a dark-themed visual HTML catalog with an analytics dashboard and a full metadata table, ready to open in any browser.

---

### Software Quality & Engineering

The project follows professional software engineering practices:

* Object-Oriented Design
* Modular Architecture
* Type Hints
* Automated Testing with Pytest
* Continuous Integration with GitHub Actions
* Service Layer Pattern
* Clean Separation of Responsibilities

Current automated test suite:

* AudioMetadata
* AudioAnalyzer
* BPMAnalyzer
* KeyAnalyzer

All tests run automatically on every push through GitHub Actions.

---

## Project Architecture

```text
audio-asset-metadata-manager
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── tests/
│   ├── test_audio_metadata.py
│   ├── test_audio_analyzer.py
│   ├── test_bpm_analyzer.py
│   └── test_key_analyzer.py
│
├── pytest.ini
│
├── audio_files/
│
├── output/
│   ├── metadata.json
│   ├── metadata.csv
│   ├── analytics.json
│   └── catalog.html
│
├── src/
│   ├── analyzers/
│   │   ├── audio_analyzer.py
│   │   ├── batch_analytics.py
│   │   ├── bpm_analyzer.py
│   │   ├── key_analyzer.py
│   │   └── metadata_parser.py
│   │
│   ├── exporters/
│   │   ├── analytics_exporter.py
│   │   ├── catalog_exporter.py
│   │   ├── csv_exporter.py
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
* Pytest
* GitHub Actions
* JSON
* CSV
* HTML

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
{'filename': '2 GMS, Dickster & Legohead - Dala.wav', 'title': 'Dala', 'artist': 'GMS & Dickster & Legohead', 'album': 'Adverse Cambers', 'genre': 'Psy-Trance', 'year': '2021', 'track_number': '4', 'duration': 368.54, 'sample_rate': 44100, 'channels': 2, 'bpm': 143.55, 'key': 'D# Minor'}

JSON exported: output/metadata.json
CSV exported: output/metadata.csv

==========================================
           BATCH ANALYTICS
==========================================
  Total de arquivos    : 1
  BPM médio            : 143.55
  BPM mais alto        : 143.55
  BPM mais baixo       : 143.55
  Duração total        : 6.14 min
  Tonalidade comum     : D# Minor
  Gêneros encontrados  : Psy-Trance
==========================================

Analytics exported: output/analytics.json
Catalog exported: output/catalog.html
```

Generated files:

* `output/metadata.json` — full metadata per file
* `output/metadata.csv` — spreadsheet-ready export
* `output/analytics.json` — batch statistics
* `output/catalog.html` — visual HTML catalog

---

## Automated Testing

The project includes automated tests using Pytest.

Run all tests:

```bash
pytest
```

Current coverage includes:

* Metadata Model
* Audio Analyzer
* BPM Detection
* Musical Key Detection

Example output:

```text
============================
4 passed
============================
```

---

## Continuous Integration

This repository uses GitHub Actions for Continuous Integration.

Every push and pull request automatically:

1. Creates a clean environment
2. Installs dependencies
3. Runs the complete test suite
4. Reports success or failure

Workflow:

```text
Push → GitHub Actions → Pytest → Build Status
```

---

## Future Enhancements

Planned features:

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
* Audio Signal Analysis
* Music Information Retrieval (MIR)
* Metadata Processing
* BPM Detection
* Musical Key Detection
* Data Analytics
* Multi-format Export (JSON, CSV, HTML)
* Automated Testing with Pytest
* Continuous Integration (CI/CD)
* Git Version Control
* GitHub Actions
* Software Engineering Best Practices

---

## Author

Norton Henrique Silva

Audio Producer, DJ, Audio Technology Enthusiast and Software Engineering Student.

GitHub: https://github.com/antiviruslive
