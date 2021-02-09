from flask import request
from functools import wraps
import requests
from setup_movie_library import *


ACCESS = {
    'user': 1,
    'admin': 2
}


def requires_access_level(access_level):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'Authorization' in request.headers:
                token = request.headers['Authorization']
                response = requests.get(
                    'http://{0}:{1}/protected'.format(app.config['USER_SERVICE_NAME'], app.config['USER_PORT']),
                    headers={'Authorization': token.__str__()}
                )
                data = response.json()

                if response.ok:
                    if(data['access'] < access_level):
                        return {"message": "access deny"}, 401
                else:
                    return response.json(), 401
            else:
                return {"message": "access deny"}, 401
            return f(*args, **kwargs)
        return decorated_function
    return decorator
