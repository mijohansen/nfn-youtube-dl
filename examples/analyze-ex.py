import json
from datetime import datetime

from notefornote import analyze_audio

start_time = datetime.now()
# output/rwipMr069dg.stereo32.opus

genres = analyze_audio("output/ihle.wav")
json_object = json.dumps(genres, indent=4)

print(json_object)
