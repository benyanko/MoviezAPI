from flask_restful import Resource, reqparse
from movie_library_models.movie_model import MovieModel
from movie_library_models.category_model import CategoryModel
from movie_library_security import *


class Movie(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('category_id',
                        type=int,
                        required=True,
                        help="Every movie needs a category id"
                        )
    parser.add_argument('video_link',
                        type=str,
                        required=True,
                        help="Every movie needs a video link"
                        )

    @requires_access_level(ACCESS['user'])
    def get(self, _id):
        movie = MovieModel.find_by_id(_id)
        if movie:
            return movie.json()
        return {'message': 'movie not found'}, 404

    @requires_access_level(ACCESS['admin'])
    def post(self, name):
        if MovieModel.find_by_name(name):
            return {'message': "movie with name '{}' allready exist".format(name)}, 400

        data = Movie.parser.parse_args()

        if CategoryModel.find_by_id(data['category_id']) is None:
            return {'message': "category not exist"}, 400

        movie = MovieModel(name, data['price'], data['video_link'], data['category_id'])

        try:
            movie.save_to_db()
        except:
            return {"message": "Error inserting item"}, 500

        return movie.json(), 201

    @requires_access_level(ACCESS['admin'])
    def delete(self, _id):
        movie = MovieModel.find_by_id(_id)
        if movie:
            movie.delete_from_db()

        return {'message': 'movie deleted'}

    @requires_access_level(ACCESS['admin'])
    def put(self, _id):

        data = Movie.parser.parse_args()

        movie = MovieModel.find_by_id(_id)

        if movie is None:
            return {'message': 'movie not found'}, 404
        else:
            movie.price = data['price']
            movie.video_link = data['video_link']
        movie.save_to_db()

        return movie.json()


class MovieList(Resource):
    @requires_access_level(ACCESS['user'])
    def get(self):
        return {'movies': [movie.json() for movie in MovieModel.query.all()]}
