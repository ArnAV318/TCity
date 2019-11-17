from flask import Flask,render_template, Blueprint, request
from app.models import Mobile_product,image_model
from app import db
from flask_login import login_user, current_user, logout_user, login_required
buy = Blueprint('buypage',__name__)

@buy.route('/buy')
@login_required
def buypage():
    productid = request.args.get('prod')
    product_type = request.args.get('type')
    print(product_type)
    print(productid)
    product = Mobile_product.query.filter_by(pid = productid).first()
    product = product.serialize()
    imgs = image_model.query.filter_by(pid=productid , product_type=product_type).all()
    imgs=list(imgs)
    x=imgs.pop(0)
    print(x)
    mproduct = product.copy()
    product.pop('pid')
    product.pop('title')
    print(product)
    uid=current_user.uid
    print("hhii"+str(uid))
    stars=int(product['rating'])
    return render_template('buypage.html', product=product, mproduct=mproduct,stars=stars, imgs=imgs, x=x,uid=uid,pid=productid,ptype=product_type)


