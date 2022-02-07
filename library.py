from app import app, db
from app.models_sqlalchemy import Book, Author, Borrow

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Book": Book,
        "Author": Author,
        "Borrow": Borrow
    }