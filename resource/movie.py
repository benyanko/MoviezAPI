from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.movie import MovieModel
from models.category import CategoryModel


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

    def get(self, _id):
        movie = MovieModel.find_by_id(_id)
        if movie:
            return movie.json()
        return {'message': 'movie not found'}, 404

    @jwt_required()
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

    @jwt_required()
    def delete(self, _id):
        movie = MovieModel.find_by_id(_id)
        if movie:
            movie.delete_from_db()

        return {'message': 'movie deleted'}

    @jwt_required()
    def put(self, _id):

        data = Movie.parser.parse_args()

        movie = MovieModel.find_by_id(_id)

        if movie is None:
            return {'message': 'movie not found'}, 404
        else:
            movie.price = data['price']
        movie.save_to_db()

        return movie.json()


class MovieList(Resource):
    def get(self):
        return {'movies': [movie.json() for movie in MovieModel.query.all()]}
