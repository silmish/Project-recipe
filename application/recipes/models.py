from application import db

from application.recipe_ingredients.models import recipe_ingredients


class Recipe(db.Model):
    __tablename__ = "Recipe"
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(60), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    recipeIngredients = db.relationship('Ingredient', secondary=recipe_ingredients,
                                        backref=db.backref('recipe_ingredient', lazy='dynamic'))

    def __init__(self, name):
        self.name = name
