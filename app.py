from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resource.user import UserRegister
from resource.movie import Movie, MovieList
from resource.category import Category, CategoryList

from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'QS3-CX5-RF9'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Category, '/category/<string:name>')
api.add_resource(Movie, '/movie/<int:_id>', '/movie/<string:name>')
api.add_resource(MovieList, '/movie')
api.add_resource(CategoryList, '/category')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)

