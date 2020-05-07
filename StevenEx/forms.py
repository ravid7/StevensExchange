from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, Form
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from StevenEx.models import User

# //Register a new user to portal through form 
class RegisterationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), 
                                            EqualTo('password')])
    submit = SubmitField('Sign Up')
    # // To check wether the username already exists in the database 
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    # // To check wether the email already exists in the database for dublication purpose 
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

# // Login to portal as a unique user 
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Always')
    submit = SubmitField('Sign In')

# // Search bar for companies 
class SearchForm(Form):
    search = StringField('Search for life.', [DataRequired()], render_kw={'class': 'form-control form-control-sm ml-3 w-75', 'placeholder': 'Search for your life'})
    submit = SubmitField('Search')

class AddLib(Form):
    submit = SubmitField('+ ADD')