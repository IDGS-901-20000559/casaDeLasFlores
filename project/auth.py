from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def index():
    return render_template('login.html')

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    return render_template('register.html')
