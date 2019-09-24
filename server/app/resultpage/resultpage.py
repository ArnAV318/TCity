from flask import Flask,render_template, Blueprint
result = Blueprint('resultpage',__name__)

@result.route('/resultpage')
def resultpage():
    return render_template('index.html')


