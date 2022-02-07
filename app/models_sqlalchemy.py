from app import db
from datetime import datetime

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), index=True, unique=True)
    origin = db.Column(db.String(50))
    books = db.relationship("Book", backref="author", lazy="dynamic")

    def __str__(self) -> str:
        return f"Autor: {self.name}"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), index=True)
    series = db.Column(db.String(300), index=True)
    pages = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    book = db.relationship("Borrow", backref="book", lazy="dynamic")

    def __str__(self) -> str:
        return f"Książka: {self.title}, {self.author}"

class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    status = db.Column(db.String(50), index=True, default="pożyczona")
    date = db.Column(db.Date, default=datetime.utcnow)

    def __str__(self) -> str:
        return f"{self.book} status: {self.status}, data: {self.date}"