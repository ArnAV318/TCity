from flask import Flask,render_template, Blueprint
import pickle
import os
from app import db
from app.models import Mobile_product

mobile_heads=['OS','RAM','Item Weight','Product Dimensions','Batteries:','Item model number','Wireless communication technologies',
'Connectivity technologies','Special features','Display technology','Other camera features','Form factor','Weight',
'Colour','Battery Power Rating','Whats in the box']


input = Blueprint('inputdatapage',__name__)

@input.route('/input')
def resultpage():
    db.create_all()
    print("done")
    pickle_in = open("datamobile.pickle","rb")
    datajson = pickle.load(pickle_in)
    print(datajson[1]['Display technology'])
    print()
    print()
    for i in range(len(datajson)):
        price=datajson[i]['price']
        price=price[2:-3]
        price="".join(filter(lambda char: char != ",", price))
        price=int(price)
        rating=datajson[i]['rating']
        rating=list(rating.split())
        rating=float(rating[0])
        print("title length "+str(len(datajson[i]['title'])))
        a = Mobile_product(datajson[i]['title'],price,rating,
            datajson[i]['OS'],datajson[i]['RAM'],datajson[i]['Item Weight'],datajson[i]['Product Dimensions'],
            datajson[i]['Batteries:'],datajson[i]['Item model number'],datajson[i]['Wireless communication technologies'],datajson[i]['Connectivity technologies'],datajson[i]['Special features'],
            datajson[i]['Display technology'],datajson[i]['Other camera features'],datajson[i]['Form factor'],datajson[i]['Colour'],
            datajson[i]['Battery Power Rating'],datajson[i]['Whats in the box'])
        db.session.add(a)
        db.session.commit()
    
    
    if len(datajson)==0:
        exit(0)
    return "hiiiiiiii"


