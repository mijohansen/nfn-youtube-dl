import os

import numpy as np
from essentia.standard import MonoLoader, TensorflowPredictEffnetDiscogs, TensorflowPredict2D

from notefornote.labels import labels


def remove_low_match(genre):
    return genre[1] >= 0.01


models_dir = os.path.dirname(__file__) + "/models/"

embeddings_model = TensorflowPredictEffnetDiscogs(
    graphFilename=models_dir + "discogs-effnet-bs64-1.pb",
    output="PartitionedCall:1"
)

classification_model = TensorflowPredict2D(
    graphFilename=models_dir + "genre_discogs400-discogs-effnet-1.pb",
    input="serving_default_model_Placeholder",
    output="PartitionedCall:0",
)


def analyze_audio(filename: str):
    audio = MonoLoader(filename=filename, sampleRate=16000, resampleQuality=4)()
    print("Audio loaded.")
    embeddings = embeddings_model(audio)
    print("Audio put into the Embeddings model.")
    activations = classification_model(embeddings)
    print("Embeddings put into the classification_model.")
    activations_mean = np.mean(activations, axis=0)

    # Parsing Genres
    result_dict = dict(zip(labels, activations_mean.tolist()))
    sorted_genres = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)
    return list(filter(remove_low_match, sorted_genres))
