from flask import Flask,render_template, Blueprint,request
from sqlalchemy import desc
result = Blueprint('resultpage',__name__)
from app import db
from app.models import Mobile_product

@result.route('/resultpage')
def resultpage():
    page = request.args.get('page', 1, type=int)
    products=Mobile_product.query.order_by(desc(Mobile_product.rating)).paginate(page=page, per_page=6)
    pproducts=list(products.items)
    i=0
    l1=[]
    l2=[]
    if len(pproducts)>3:
        while len(pproducts)<6:
            pproducts.append(0)
        for i in range(6):
            if i<3:
                l1.append(pproducts.pop(0))
            else:
                l2.append(pproducts.pop(0))
        pproducts.append(l1)
        pproducts.append(l2)
    else:
        while len(pproducts)<3:
            pproducts.append(0)
        for i in range(3):
            if i<3:
                l1.append(pproducts.pop(0))
        pproducts.append(l1)
    
    print(pproducts[0][0].title)
        

    return render_template('result.html',pproduct=pproducts,product=products)


