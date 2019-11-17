from flask import Flask,render_template, Blueprint,request,request
from sqlalchemy import desc
result = Blueprint('resultpage',__name__)
from app import db
from app.models import Mobile_product,Tv_product,image_model

@result.route('/resultpage' ,methods=["POST","GET"])
def resultpage():
    query = request.form.get('searchy')
    


    page = request.args.get('page', 1, type=int)
    if isinstance(query,str):
        if query.lower()=="tv":
            products=Tv_product.query.order_by(desc(Tv_product.rating)).paginate(page=page, per_page=6)
            pproducts=list(products.items)
        elif query.lower()=="mobile":
            products=Mobile_product.query.order_by(desc(Mobile_product.rating)).paginate(page=page, per_page=6)
            pproducts=list(products.items)
    else:
        products=Tv_product.query.order_by(desc(Tv_product.rating)).paginate(page=page, per_page=6)
        pproducts=list(products.items)
    listy=[]
    for a in pproducts:
        star=[0]*int(a.rating)
        x=image_model.query.filter_by(pid=a.pid , product_type=a.product_type).first()
        listy.append([a,x,star])
    i=0
    l1=[]
    l2=[]
    if len(pproducts)>3:
        while len(pproducts)<6:
            listy.append(0)
        for i in range(6):
            if i<3:
                l1.append(listy.pop(0))
            else:
                l2.append(listy.pop(0))
        listy.append(l1)
        listy.append(l2)
    else:
        while len(pproducts)<3:
            listy.append(0)
        for i in range(3):
            if i<3:
                l1.append(listy.pop(0))
        listy.append(l1)
    
    print(listy[0][0][1])
    
        

    return render_template('result.html',listy=listy,product=products)


