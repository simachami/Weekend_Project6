from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager



@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


class User(UserMixin,db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    username = db.Column(db.String(100), nullable = False, unique = True)
    email = db.Column(db.String(180), nullable = False, unique = True)
    password_hash = db.Column(db.String(), nullable = False)
    pokemons = db.relationship('Pokemon', backref = 'author', lazy=True)


    def to_dict(self):
        return {
            'first_name': self.first_name,     
            'last_name': self.last_name,
            'email': self.email,
            'username': self.username,
            'pokemon': [{
            'body':post.body, 
            'timestamp':post.timestamp
        } for post in self.posts ]
        }


    def __repr__(self):
        return f'<User: {self.username}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def from_dict(self, user_obj):
        for attribute, value in user_obj.items():
            setattr(self, attribute, value)

    def get_id(self):
        return str(self.user_id)

    def hash_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)
    
class Pokemon(db.Model):
    pokemon_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)
    weight = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable= False)

    def __repr__(self):
        return f'<Pokemon: {self.name}>'
    

    def commit(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()
