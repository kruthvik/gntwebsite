from flask import Flask
from .views import blueprint
import os

port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
app.run(host='0.0.0.0', port=port, debug=True)

app.register_blueprint(blueprint)


def start():
    app.run(debug=True)
