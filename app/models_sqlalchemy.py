from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), index=True)
    author = db.Column(db.String(200), index=True)
    series = db.Column(db.String(300), index=True)
    pages = db.Column(db.Integer)
    cover = db.Column(db.String(10))

    def __str__(self) -> str:
        return f"Book {self.title} {self.author}"
