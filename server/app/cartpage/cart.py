from flask import Flask,render_template, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
cart = Blueprint('cartpage',__name__)


@cart.route('/cart')
@login_required
def cartpage():
    return render_template('cartpage.html')


