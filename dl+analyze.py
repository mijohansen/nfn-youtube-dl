import json
import tempfile
from notefornote import download_audio, analyze_audio

target_dir = tempfile.TemporaryDirectory()
filepath = download_audio("youtube", "c0-hvjV2A5Y", target_dir.name)
genres = analyze_audio(filepath)
json_object = json.dumps(genres, indent=4)
print(json_object)
