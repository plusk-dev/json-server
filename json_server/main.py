import click
import json
from flask import Flask,make_response
from flask.json import jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


class InvalidJson(Exception):
    pass

@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.argument('port', default=5000)
def cli_command(filename, port):

    @app.route("/", methods=["GET"])
    def index():
        with open(click.format_filename(filename)) as f:
            try:
                contents = json.loads(f.read())
            except json.JSONDecodeError as e:
                raise InvalidJson("Enter a proper JSON file")
            response = make_response((json.dumps(contents,indent=4)))
            response.content_type = "application/json"
            return response

    app.run(debug=True, port=port)
