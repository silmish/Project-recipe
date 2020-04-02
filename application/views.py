from flask import render_template
from application import app
from application.recipes.models import Recipe


@app.route("/")
def index():
    return render_template("index.html", has_ingredients=Recipe.find_recipes_with_ingredients())
