from application import db

favorites = db.Table('favorites',
                     db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
                     db.Column('account_id', db.Integer, db.ForeignKey('account.id'))
                     )
