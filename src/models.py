from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__: "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    fav_movies = db.relationship("FavoriteMovies", backref="fav_movies")

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "fav_movies":  [fav.serialize() for fav in self.fav_movies]
        }

class Movies(db.Model):
    __tablename__: "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    genre = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Movies %r>' % self.title

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre
        }


class FavoriteMovies(db.Model):
    __tablename__ = 'favorite_movies'
    #id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    movies_id = db.Column(db.Integer, db.ForeignKey("movies.id"), primary_key=True)

    def serialize(self):
        return {
            "user_id": self.user_id ,
            "movies_id": self.movies_id
        }