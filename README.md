# MoviezAPI
## Table of contents
* [General info](#general-info)
* [Description](#description)
* [Task list](#task-list)

## General info
This project implement Movie library management platform RESTful API using Flask-RESTful, SQLAlchemy and JWT. A simple user can browse the movie library and get information about each movie while an admin user gets permission to manage the movie library when he can add edit and delete movies and categories.

## Description
Description for each file:

MovieLibraryMicroservice:

movie_library_models:
* category_model -  CategoryModel fields are id, name. in addition contains a movies field which contains all the movies belonging to it implement by one-to-many relationship
* movie_model -  MovieModel fields are id, name, price, video_link. in addition contains a category_id field which contains the id category which it is associated implement by many-to-one relationship

movie_library_resource: 
* category_resource -  Category implement HTTP request methods such as get, post, delete. 
* movie_resource -  Movie implement HTTP request methods such as get, post, delete, put. 

setup_movie_library:
* config - Set all the necessary settings.

Additional files:
* main_movie_library - Create a Flask app with all the required routes.
* movie_library_db - An abstract object for SQLAlchemy implementation.
* movie_library_security - Security decorator for checking user accsess level.

UserMicroservice:

models:
* user_model -  UserModel fields are id, name, password,

resource: 
* user_resource -  Movie implement post HTTP request method. 

setup_user:
* config - Set all the necessary settings.

Additional files:
* main_user - Create a Flask app with all the required routes.
* user_db - An abstract object for SQLAlchemy implementation.
* user_security - Contains authenticate and identity methods for JWT.


## Task list
- [x] JWT
- [x] Database Relationships
- [x] Docker
- [ ] Recommender system


