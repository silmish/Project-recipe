from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from application import app, db
from application.recipe_ingredients.models import recipe_ingredients
from application.recipes.models import Recipe
from application.ingredients.models import Ingredient
from application.recipes.forms import RecipeForm
from application.recipes.updateform import UpdateForm
from application.recipes.deleteform import DeleteForm


@app.route("/recipes", methods=["GET"])
def recipes_index():
    recipeList = Recipe.find_recipes_with_ingredients()

    return render_template("recipes/list.html", has_ingredients=recipeList)


@app.route("/recipes/<recipe_id>", methods=["GET"])
@login_required
def recipes_by_id(recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    ingredients = Ingredient.query.join(recipe_ingredients).join(Recipe) \
        .filter((recipe_ingredients.c.recipe_id == recipe.id) &
                (recipe_ingredients.c.ingredients_id == Ingredient.id)).all()

    return render_template("recipes/recipe.html", recipe=recipe, ingredients=ingredients)


@app.route("/recipes/new/")
@login_required
def recipes_form():
    return render_template("recipes/new.html", form=RecipeForm())


@app.route("/recipes/new/", methods=["POST", "GET"])
@login_required
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form=form)

    r = db.session.query(Recipe).filter(Recipe.name == form.name.data).one_or_none()

    if r is not None:
        flash("Recipe you are trying to add already exists", "warning")
    elif form.name.data.__len__() < 2:
        flash("Recipe name has to be longer than 1 character", "warning")
    else:
        flash("Recipe has been added", "success")
        t = Recipe(form.name.data)
        t.account_id = current_user.id
        db.session().add(t)

        ingredients_string = form.ingredientString.data

        ingredients = [x.strip() for x in ingredients_string.split(',')]

        for ingredient in ingredients:
            x = db.session.query(Ingredient).filter(Ingredient.name == ingredient).one_or_none()

            if not x:
                if ingredient.__len__() < 2:
                    flash("Ingredient name has to be longer than 1 character", "warning")
                else:
                    x = Ingredient(ingredient)
                    db.session().add(x)

            t.recipeIngredients.append(x)

    try:
        db.session().commit()
    except Exception as e:
        print(str(e))

    return redirect(url_for("recipes_create"))


@app.route("/recipes/update/", methods=["POST", "GET"])
@login_required
def recipes_update():
    form = UpdateForm(request.form)

    if not form.validate():
        return render_template("recipes/update.html", form=form)

    update = Recipe.query.filter_by(name=form.name.data).first()

    if update is None:
        flash("Recipe you are trying to update do not exist", "warning")
    elif update.account_id != current_user.id:
        flash("You can only update recipes you have added yourself", "danger")
    elif form.name.data.__len__() < 2 or form.new.data.__len__() < 2:
        flash("Recipe name has to be longer than 1 character", "danger")
    else:
        flash("Recipe name has been updated", "success")
        update.name = form.new.data
        db.session().commit()

    return redirect(url_for("recipes_update"))


@app.route("/recipe/delete/", methods=["POST", "GET"])
@login_required
def recipes_delete():
    form = DeleteForm(request.form)

    if not form.validate():
        return render_template("recipes/delete.html", form=form)

    remove = Recipe.query.filter_by(name=form.name.data).first()

    if remove is None:
        flash("Recipe you are trying to delete do not exist", "warning")
    elif remove.account_id != current_user.id:
        flash("You can only delete recipes you have added yourself", "danger")
    else:
        flash("Recipe has been deleted", "success")
        db.session().delete(remove)
        db.session().commit()

    return redirect(url_for("recipes_delete"))
