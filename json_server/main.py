import click
import json
from flask import Flask
from flask.json import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.argument('port', default=5000)
def cli_command(filename, port):

    @app.route("/", methods=["GET"])
    def index():
        with open(click.format_filename(filename)) as file:
            contents = json.loads(file.read())
        return jsonify(contents)

    app.run(debug=True, port=port)
