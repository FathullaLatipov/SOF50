from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired


# Форма для регистрации
class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired('Заполните имя')])
    email = EmailField('Email', validators=[DataRequired('Заполните почту')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполни пароль')])
    password2 = PasswordField('Подтвердите пароль', validators=[DataRequired('Заполни пароль')])
    button = SubmitField('Зарегистрироваться')


# Форма для логина
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired('Заполните почту')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполни пароль')])
    button = SubmitField('Войти')
