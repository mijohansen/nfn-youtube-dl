from essentia.standard import MonoLoader, TensorflowPredictEffnetDiscogs,TensorflowPredict2D
from datetime import datetime
import numpy as np
from labels import labels

start_time = datetime.now()

audio = MonoLoader(filename="output/test.m4a", sampleRate=16000, resampleQuality=4)()
model = TensorflowPredictEffnetDiscogs(
    graphFilename="discogs-effnet-bs64-1.pb",
    output="PartitionedCall:1"
)
classification_model = TensorflowPredict2D(
    graphFilename="genre_discogs400-discogs-effnet-1.pb",
    input="serving_default_model_Placeholder",
    output="PartitionedCall:0",
)

embeddings = model(audio)
activations = classification_model(embeddings)
activations_mean = np.mean(activations, axis=0)

# Parsing Genres
result_dict = dict(zip(labels, activations_mean.tolist()))
sorted_genres = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)
top_genre = sorted_genres[0][0]
genre_primary, genre_full = map(str.strip, top_genre.split("---"))
genre_secondary_full = sorted_genres[1][0]
genre_secondary = genre_secondary_full.split("---")[1].strip()
print(genre_primary)
print(genre_secondary)
print(datetime.now() - start_time)
