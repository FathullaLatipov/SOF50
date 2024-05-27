from flask import Flask, render_template, request, redirect, url_for

from admin.admin import admin_bp
from users.user import user_bp

app = Flask(__name__)

app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'asndfiyadfg6879asvfg7ahvg'

app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)


# endpoint or url (urls.py)
@app.route('/')
def home():
    return render_template('index.html')


app.run(debug=True)
