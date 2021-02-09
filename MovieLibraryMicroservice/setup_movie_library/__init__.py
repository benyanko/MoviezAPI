from flask import Flask
from movie_library_db import db

app = Flask(__name__)

app.config.from_pyfile('config.py')


@app.before_first_request
def create_tables():
    db.create_all()



