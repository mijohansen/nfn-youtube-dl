import flask
import functions_framework


@functions_framework.http
def hello(request: flask.Request) -> flask.typing.ResponseReturnValue:
    return "<p>Hello, World!</p>"
