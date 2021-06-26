from typing import Text
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, RadioField
from wtforms.validators import InputRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[
                            InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[
                             InputRequired('Enter user password')])
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    role = RadioField(
        "Role", choices=[('administrator', 'Administrator'), ('customer', 'Customer')], validators=[InputRequired()])
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[
                           Email("Please enter a valid email")])
    password = PasswordField("Password", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password", validators=[InputRequired()])
    phonenumber = StringField("Phone Number")
    address = StringField("Address")

    submit = SubmitField("Register")
