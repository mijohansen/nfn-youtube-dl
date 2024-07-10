import json
from datetime import datetime

from notefornote import analyze_audio_mood

start_time = datetime.now()
# output/rwipMr069dg.stereo32.opus

analysis_data = analyze_audio_mood("../output/rwipMr069dg.stereo32.opus")
json_object = json.dumps(analysis_data, indent=4)

print(json_object)
