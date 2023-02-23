from flask import render_template, Blueprint

carbon_app = Blueprint('carbon_app',__name__)


@carbon_app.route('/Carbon App')
def Carbon_app():
    return render_template('carbon_app/carbon_app.html', title='Carbon App')

@carbon_app.route('/Carbon App/new entry')
def New_entry():
    return render_template('carbon_app/new_entry.html', title='New entry')

@carbon_app.route('/Carbon App/your data')
def Your_data():
    return render_template('carbon_app/your_data.html', title='Your data')
