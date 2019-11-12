from flask import Flask,render_template, Blueprint, request
from app.models import Mobile_product
from app import db
buy = Blueprint('buypage',__name__)

@buy.route('/buy')
def buypage():
    productid = request.args.get('prod')
    print(productid)
    product = Mobile_product.query.filter_by(pid = productid).first()
    product = product.serialize()
    mproduct = product.copy()
    product.pop('pid')
    product.pop('title')
    print(product)
    stars=int(product['rating'])
    return render_template('buypage.html', product=product, mproduct=mproduct,stars=stars)


