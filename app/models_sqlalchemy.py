from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), index=True, unique=True)
    origin = db.Column(db.String(50))
    books = db.relationship("Book", backref="author", lazy="dynamic")

    def __str__(self) -> str:
        return f"Autor {self.name}"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), index=True)
    series = db.Column(db.String(300), index=True)
    pages = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))

    def __str__(self) -> str:
        return f"Book {self.title} {self.author}"