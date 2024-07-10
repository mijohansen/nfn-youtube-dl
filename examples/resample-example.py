from notefornote import resample_audio, print_json

resampled_filepath = "output/rwipMr069dg.mono32.opus"
metadata = resample_audio("output/rwipMr069dg._org.opus", resampled_filepath)

print_json(metadata)
