from app import app

@app.route("/")
def hello():
    return "Library 2.0"