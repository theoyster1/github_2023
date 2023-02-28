
from flask import render_template, Blueprint

users = Blueprint('users',__name__)


@users.route('/users')
def Register():
  return render_template('register.html', title='Register')



@users.route('/users/login')
def Login():
    return render_template('login.html', title='Login')
