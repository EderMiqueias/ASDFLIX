from flask import Flask


app = Flask(__name__)

from app.util_db import tables
from app.controller import GenresController
from app.controller import ActorsController
from app.controller import MoviesController


