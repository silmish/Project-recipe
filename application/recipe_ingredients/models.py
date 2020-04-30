from application import db

recipe_ingredients = db.Table('recipe_ingredients',
                              db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
                              db.Column('ingredients_id', db.Integer, db.ForeignKey('ingredients.id'))
                              )
