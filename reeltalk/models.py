from reeltalk import db
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import func


class User(db.Model, UserMixin):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False) 
    reviews = db.relationship('Review', backref='user', lazy=True, cascade="all, delete")

    def __repr__(self):
        return f"#{self.id}|first_name: {self.first_name}| last_name:{self.last_name}| email{self.email}"


class Movie(db.Model):
    # schema for the Movie model
    id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    overview = db.Column(db.Text)
    release_date = db.Column(db.Date)
    backdrop_path = db.Column(db.String(255))
    reviews = db.relationship('Review', backref='movie', lazy=True, cascade="all, delete")

    def __repr__(self):
        return (f"<Movie id={self.id}| tmdb_id={self.tmdb_id}| title={self.title} "
                f"release_date={self.release_date}>")


class Review(db.Model):
    # schema for the Review model
    id = db.Column(db.Integer, primary_key=True)
    # ondelete="CASCADE" added. If either a User or Movie is removed from the db then all corresponding reviews are also removed
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id', ondelete="CASCADE"), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())

    def __repr__(self):
        return (f"<Review id={self.id}| user_id={self.user_id}| movie_id={self.movie_id} "
                f"created_at={self.created_at}>")


