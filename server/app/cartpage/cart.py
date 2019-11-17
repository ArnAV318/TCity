from flask import Flask,render_template, Blueprint,request
from flask_login import login_user, current_user, logout_user, login_required
from app.models import Tv_product,Mobile_product,image_model
cart = Blueprint('cartpage',__name__)


@cart.route('/cart')
@login_required
def cartpage():
    print('hi')
    uid = request.args.get('userid')
    pid =  request.args.get('productid')
    product_type = request.args.get('type')
    if product_type=="mobile":
        product = Mobile_product.query.filter_by(pid = pid).first()
    else:
        product = Tv_product.query.filter_by(pid = pid).first()
    imgs = image_model.query.filter_by(pid=pid , product_type=product_type).first()
    product = product.serialize()
    return render_template('cartpage.html',product=product,img=imgs)


