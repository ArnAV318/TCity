from flask import Flask,render_template, Blueprint
import pickle
import os
from app import db
from app.models import Book


input = Blueprint('inputdatapage',__name__)

@input.route('/input')
def resultpage():
    db.create_all()
    print("done")
    pickle_in = open("datajson.pickle","rb")
    datajson = pickle.load(pickle_in)
    print(datajson[0]["comments"])
    
    if len(datajson)==0:
        exit(0)
    return "hiiiiiiii"


