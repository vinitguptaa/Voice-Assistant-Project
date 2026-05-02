# VoceAssistant (Jarvis)

> A simple voice assistant in Python that listens for the wake word "Jarvis" and executes basic commands (open websites, tell time, play songs from the included music library, and search Wikipedia).

## Files

- `main.py` - main voice assistant program (speech recognition, intent parsing, and action handlers).
- `musicLibrary.py` - small mapping of song names to YouTube links used by the assistant.

## Quick Start

1. Create and activate a virtual environment (recommended).

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install speechrecognition pyttsx3 wikipedia nltk pyaudio
```

Note: On Windows, installing `pyaudio` may require a prebuilt wheel if your system lacks build tools.

3. Run the assistant:

```powershell
python main.py
```

Say the wake word `Jarvis`, then speak a command (for example: "Jarvis, open YouTube" or "Jarvis, play kamleya").

## Music Library

Edit `musicLibrary.py` to add or change song name -> URL mappings. The assistant expects a single-word song token at the end of the spoken command.

## Notes

- The project uses `nltk` tokenization; the first run may download NLTK data (see `main.py`).
- Microphone access is required; ensure your OS and Python environment can access audio input.

## Contributing

Feel free to open issues or PRs. If you want me to create a `requirements.txt` or add a Windows-friendly `pyaudio` wheel helper, tell me and I will add it.
