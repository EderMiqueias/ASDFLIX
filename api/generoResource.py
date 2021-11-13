from flask import Flask, jsonify, request
from repository import GeneroRepository

app = Flask(__name__)


@app.route("/genero", methods=['GET', 'POST', 'PUT', 'DELETE'])
def genero():
    if request.method == 'GET':
        repo = GeneroRepository()
        generos = repo.get_generos()
        responses = jsonify(generos)
        responses.status_code = 200
        return responses

app.run()
