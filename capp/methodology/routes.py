from flask import render_template, Blueprint

methodology = Blueprint('methodology',__name__)


@methodology.route('/methodology')
def Methodology():
  return render_template('Methodology.html', title='Methodology')