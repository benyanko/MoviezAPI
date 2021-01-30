from db import db


class MovieModel(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    video_link = db.Column(db.String(80))

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('CategoryModel')

    def __init__(self, name, price, video_link, category_id):
        self.name = name
        self.price = price
        self.video_link = video_link
        self.category_id = category_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'video_link': self.video_link}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def delete_list_from_db(cls, movies):
        for movie in movies:
            db.session.delete(movie)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()




