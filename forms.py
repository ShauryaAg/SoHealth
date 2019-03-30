from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField, SelectField, TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from SoHealth.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


choices=  [
    {
        'activity': 'Walking',
        'calories': 7.6
    },
    {
        'activity': 'Running',
        'calories': 13.2
    },
    {
        'activity': 'Football',
        'calories': 12
    },
    {
        'activity': 'Basketball',
        'calories': 9.33
    },
    {   'activity': 'Tennis',
        'calories': 9.33
    }]

class PostForm(FlaskForm):
    activity =  SelectField('Activity', choices =[('value', 'Walking'), ('value_two', 'Running'),
                                        ('value_three', 'Football'), ('value_four', 'Basketball'), ('value_five', 'Tennis')],)
    StartTime = TimeField('Start',  validators=[DataRequired()])
    EndTime =  TimeField('End', validators=[DataRequired()])
    title = StringField('Activity Title', validators=[DataRequired()])
    content = TextAreaField('Notes', validators=[DataRequired()])
    submit = SubmitField('POST')
