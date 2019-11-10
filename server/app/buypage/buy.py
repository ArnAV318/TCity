from flask import Flask,render_template, Blueprint
buy = Blueprint('buypage',__name__)

@buy.route('/buy')
def resultpage():
    return render_template('buypage.html')


