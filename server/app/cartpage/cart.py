from flask import Flask,render_template, Blueprint
cart = Blueprint('cartpage',__name__)

@cart.route('/cart')
def resultpage():
    return render_template('cartpage.html')


