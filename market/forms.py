from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_adress(self, email_to_check):
        email_adress = User.query.filter_by(email_adress=email_to_check.data).first()
        if email_adress:
            raise ValidationError('Email Adress already exists! Please try a different email adress')

    username = StringField(label='User Name:', validators=[Length(min=6, max=30), DataRequired()])
    email_adress = StringField(label='Email Adress:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')