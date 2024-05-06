import flask
from flask import jsonify
import functions_framework
from notefornote import download_audio, analyze_audio


@functions_framework.http
def hello(request: flask.Request) -> flask.typing.ResponseReturnValue:
    filepath = download_audio("soundcloud", "zZeY7rWqdncdKq8d7")
    genres = analyze_audio(filepath)
    return jsonify(genres)
