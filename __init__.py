from flask import Flask
from . import webInterface

def create_app():
    app=Flask(__name__)
    app.register_blueprint(webInterface.bp)

    return app
    