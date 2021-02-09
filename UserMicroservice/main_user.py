from flask_restful import Api
from flask_jwt import JWT

from setup_user import *
from user_db import db
from resource.user_resource import UserRegister, UserLoggedIn
from user_security import authenticate, identity


api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth
api.add_resource(UserRegister, '/register')
api.add_resource(UserLoggedIn, '/protected')
db.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['USER_PORT'])
