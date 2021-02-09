from flask_restful import Api

from setup_movie_library import *
from movie_library_db import db
from movie_library_resource.movie_resource import Movie, MovieList
from movie_library_resource.category_resource import Category, CategoryList


api = Api(app)

api.add_resource(Category, '/category/<string:name>')
api.add_resource(Movie, '/movie/<int:_id>', '/movie/<string:name>')
api.add_resource(MovieList, '/movie')
api.add_resource(CategoryList, '/category')
db.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['MOVIE_LIBRARY_PORT'])