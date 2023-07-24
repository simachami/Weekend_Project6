from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[ DataRequired()])
    password = PasswordField('Password:', validators=[ DataRequired()])
    submit = SubmitField('Sign In')


class SignUpForm(FlaskForm):
    first_name = StringField('First Name: ')
    last_name = StringField('Last Name: ')
    username = StringField('Username:',validators=[ DataRequired() ])
    email = StringField('Email:', validators=[ DataRequired() ])
    password = PasswordField('Password:', validators=[ DataRequired() ])
    verify_password = PasswordField('Confirm Password:', validators=[ DataRequired(), EqualTo('password') ])
    submit = SubmitField('Sign Up')


class PokemonForm(FlaskForm):
    name = StringField('Add a Pokemon:', validators=[DataRequired()])
    submit = SubmitField('Add')


class UserSearchForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Delete Pokemon')
