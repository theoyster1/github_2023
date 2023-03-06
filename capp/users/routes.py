
from flask import render_template, Blueprint, redirect, flash, url_for

from capp.users.forms import LoginForm, RegisterForm

users = Blueprint('users',__name__)


@users.route('/users', methods = ['GET', 'POST'])
def Register():
  form = RegisterForm()
  if form.validate_on_submit():
    flash('Successfully registred', 'success')
    return redirect(url_for('home.Home'))
  return render_template('register.html', title='Register', form = form)

@users.route('/users/login', methods=['GET', 'POST'])
def Login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.username.data == 't1' and form.password.data == 't1':
      flash('Succesfully logged in', 'success')
      return redirect(url_for('home.Home'))
    else: flash('Wrong username or password', 'danger')
  return render_template('login.html', title='Login', form=form)
