from datetime import datetime
import json
from notefornote import analyze_audio


start_time = datetime.now()
genres = analyze_audio("output/test.m4a")
json_object = json.dumps(genres, indent=4)

print(json_object)

