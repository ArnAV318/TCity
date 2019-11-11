from flask import Flask,render_template, Blueprint
result = Blueprint('resultpage',__name__)
from app import db
from app.models import Mobile_product

@result.route('/resultpage')
def resultpage():
    products=Mobile_product.query.order_by()
    print(products[0].title)
    
    return render_template('result.html')


