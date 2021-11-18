from flask import Flask
from app.util_db import tables
from app.controller import GenresController
from app.controller import ActorsController
from app.controller import MoviesController

app = Flask(__name__)
