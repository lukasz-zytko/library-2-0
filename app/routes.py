from app import app, models_sqlite, forms
from flask import render_template, request

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/<table_name>", methods=["GET", "POST"])
def table(table_name):
    models_sqlite.table.create_connection()
    results = models_sqlite.table.get_table(table_name)
    if table_name == "book":
        form = forms.BookForm()
    elif table_name == "author":
        form = forms.AuthorForm()
    elif table_name == "borrow":
        form = forms.BorrowForm()
    if request.method == "POST":
        if form.validate_on_submit():
            models_sqlite.table.create_connection()
            models_sqlite.table.add(table_name,form.data)
    return render_template(f"{table_name}s.html", results=results, form=form)

