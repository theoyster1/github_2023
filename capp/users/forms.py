from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', 
                           validators = [DataRequired()])
    password = PasswordField('Password',
                             validators = [DataRequired()])
    submit = SubmitField('Log in')
    
class RegisterForm(FlaskForm):
    username = StringField('Username', 
                        validators = [DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    password = PasswordField('Password',
                            validators = [DataRequired()])
    
    confirm_password = PasswordField('Confirm Password', 
                                     validators=[DataRequired(), 
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')

    

