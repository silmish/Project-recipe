from application import db

"""recipe_ingredients = db.Table('recipe_ingredients',
                              db.Column('recipe_id', db.Integer, db.ForeignKey('Recipe.id')),
                              db.Column('ingredients_id', db.Integer, db.ForeignKey('ingredients.id'))
                              )"""


class RecipeIngredient(db.Model):
    __tablename__ = "recipe_ingredients"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    ingredients_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), nullable=False)

    def __init__(self, recipe_id, ingredients_id):
        self.recipe_id = recipe_id
        self.ingredients_id = ingredients_id
