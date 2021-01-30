# MoviezAPI
## Table of contents
* [General info](#general-info)
* [Description](#description)
* [Task list](#task-list)

## General info
This project implement Movie library management platform RESTful API. A simple user can browse the movie library and get information about each movie while an admin user gets permission to manage the movie library when he can add edit and delete movies and categories.

## Description
Description for each file:

models:
* category -  CategoryModel fields are id, name. in addition contains a movies field which contains all the movies belonging to it implement by one-to-many relationship
* movie -  MovieModel fields are id, name, price, video_link. in addition contains a category_id field which contains the id category which it is associated implement by many-to-one relationship
* user -  UserModel fields are id, name, password,

resource: 
* category -  Category implement HTTP request methods such as get, post, delete. 
* movie -  Movie implement HTTP request methods such as get, post, delete, put. 
* user -  Movie implement post HTTP request method. 

Additional files:
* db - An abstract object for SQLAlchemy implementation.
* security - Contains authenticate and identity methods for JWT.
* app - create and set all the necessary settings.
## Task list
- [x] JWT
- [x] Database Relationships
- [ ] Recommender system


