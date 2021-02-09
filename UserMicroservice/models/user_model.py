from user_db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    access = db.Column(db.Integer)

    def __init__(self, username, password, access):
        self.username = username
        self.password = password
        self.access = access

    def json(self):
        return {'id': self.id,'username': self.username, 'password': self.password, 'access': self.access}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
       return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


