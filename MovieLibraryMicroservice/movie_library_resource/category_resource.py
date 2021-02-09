from flask_restful import Resource
from movie_library_models.category_model import CategoryModel
from movie_library_models.movie_model import MovieModel
from movie_library_security import *


class Category(Resource):

    @requires_access_level(ACCESS['user'])
    def get(self, name):
        category = CategoryModel.find_by_name(name)
        if category:
            return category.json()
        return {'message': 'category not found'}, 404

    @requires_access_level(ACCESS['admin'])
    def post(self, name):
        if CategoryModel.find_by_name(name):
            return {'message': 'A category with name {} already exists'.format(name)}, 400

        category = CategoryModel(name)
        try:
            category.save_to_db()
            return category.json()
        except:
            return {'message': 'An error create category'}, 500

    @requires_access_level(ACCESS['admin'])
    def delete(self, name):
        category = CategoryModel.find_by_name(name)
        if category:
            MovieModel.delete_list_from_db(category.movies)
            category.delete_from_db()
        return {'message': 'category deleted'}


class CategoryList(Resource):
    @requires_access_level(ACCESS['user'])
    def get(self):
        return {'categories': [category.json() for category in CategoryModel.query.all()]}