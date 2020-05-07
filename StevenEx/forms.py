from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, Form
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from StevenEx.models import User

#Registering the user
class RegisterationForm(FlaskForm):
    #defining validators for Username, email, password,confirm password- 
    # we have to make sure we don't forget Equal to in confirm pass
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # equal to checklist - Done( FOI )
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), 
                                            EqualTo('password')])
    submit = SubmitField('Sign Up')

    #validating user name raise error if already exist
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is not available. Please choose a different one.')
    #validating email rasie error if already exist
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken. Please choose a different one.')
# Login form ( validator - Data must be required)
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Always')
    submit = SubmitField('Sign In')

class SearchForm(Form):
    search = StringField('Search for life.', [DataRequired()], render_kw={'class': 'form-control form-control-sm ml-3 w-75', 'placeholder': 'Search for your life'})
    submit = SubmitField('Search')

class AddLib(Form):
    submit = SubmitField('+ ADD')