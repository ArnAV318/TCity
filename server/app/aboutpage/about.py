from flask import Flask,render_template, Blueprint
about = Blueprint('aboutpage',__name__)

@about.route('/about')
def resultpage():
    return render_template('about.html')


