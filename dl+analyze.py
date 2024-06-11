import json
import tempfile

from notefornote import download_audio, analyze_audio

target_dir = tempfile.TemporaryDirectory()
filepath = download_audio("youtube", "pZSUbUXqR6o", target_dir.name)
genres = analyze_audio(filepath)
json_object = json.dumps(genres, indent=4)
print(json_object)

