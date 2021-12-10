from flask import Flask
from .views import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint)


def start():
    app.run(debug=True)
