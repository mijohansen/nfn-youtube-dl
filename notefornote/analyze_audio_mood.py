import os

from essentia.standard import MonoLoader, TensorflowPredict2D, TensorflowPredictMusiCNN

models_dir = os.path.dirname(__file__) + "/models/"


embeddings_model = TensorflowPredictMusiCNN(
    graphFilename=models_dir + "msd-musicnn-1.pb", output="model/dense/BiasAdd"
)

prediction_model = TensorflowPredict2D(
    graphFilename=models_dir + "moods_mirex-msd-musicnn-1.pb",
    input="serving_default_model_Placeholder",
    output="PartitionedCall"
)


def analyze_audio_mood(filename: str):
    audio = MonoLoader(filename=filename, sampleRate=16000, resampleQuality=4)()
    embeddings = embeddings_model(audio)
    predictions = prediction_model(embeddings)

    return predictions.tolist()
