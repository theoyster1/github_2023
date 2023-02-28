from flask import render_template, Blueprint

home = Blueprint('home',__name__)

@home.route('/')
@home.route('/home')
def Home():
  return render_template('Home.html', title="Home")