from flask import Blueprint, render_template
from users.forms import RegisterForm, LoginForm

# Наш bp             наша страница
user_bp = Blueprint('users', __name__, url_prefix='/user')


@user_bp.route('/')
def home_user():
    reg_url = '<br><a href="/user/register">Зарегистрироваться</a><br>'
    login_url = '<a href="/user/login">Логин</a><br>'
    return f'Добро пожловать на наш сайт и выберите страницу {reg_url + login_url}'


# Ссылка для обработки регистрации
@user_bp.route('/register')
def register_user():
    # Вызываем нашу форму
    form = RegisterForm()

    return render_template('register.html', form=form)


# Ссылка для обработки логина
@user_bp.route('/login')
def login_user():
    # Вызываем нашу форму для логина
    form = LoginForm()
    return render_template('login.html', form=form)
