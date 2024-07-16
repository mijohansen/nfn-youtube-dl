import tempfile

import flask
from flask import jsonify

from notefornote import download_audio, analyze_audio

embeddings_model = None
classification_model = None


def handler(request: flask.Request) -> flask.typing.ResponseReturnValue:
    global embeddings_model, classification_model
    target_dir = tempfile.TemporaryDirectory()
    filepath = download_audio("youtube", "p8HoEvDh70Y", {}, target_dir.name)
    genres = analyze_audio(filepath, embeddings_model, classification_model)
    # print(os.environ)
    return jsonify(genres)
