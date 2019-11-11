from app import db

class Mobile_product(db.Model):
    __tablename__ = 'mobile_product'

    pid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    price = db.Column(db.Integer())
    rating = db.Column(db.Float())
    os = db.Column(db.String(50))
    ram = db.Column(db.String(50))
    item_weight = db.Column(db.String(50))
    product_dimensions = db.Column(db.String(50))
    batteries = db.Column(db.String(300))
    item_model_no = db.Column(db.String(50))
    wireless_communication_tech = db.Column(db.String(300))
    connectivity_tech = db.Column(db.String(300))
    special_features = db.Column(db.String(300))
    display_tech = db.Column(db.String(300))
    camera_features = db.Column(db.String(300))
    form_factor = db.Column(db.String())
    color = db.Column(db.String(100))
    battery_rating = db.Column(db.String(200))
    box_contents = db.Column(db.String(300))





    def __init__(self, title, price, rating, os, ram, item_weight, product_dimensions, batteries, item_model_no, wireless_communication_tech, connectivity_tech, special_features, display_tech, camera_features, form_factor, color, battery_rating, box_contents):
        self.title = title
        self.price = price
        self.rating = rating
        self.os = os
        self.ram = ram
        self.item_weight = item_weight
        self.product_dimensions = product_dimensions
        self.batteries = batteries
        self.item_model_no = item_model_no
        self.wireless_communication_tech = wireless_communication_tech
        self.connectivity_tech = connectivity_tech
        self.special_features = special_features
        self.display_tech = display_tech
        self.camera_features = camera_features
        self.form_factor = form_factor
        self.color = color
        self.battery_rating=battery_rating
        self.box_contents = box_contents
    

    def __repr__(self):
        return '<id {} name {}>'.format(self.pid,self.title)

    def serialize(self):
        return {
            'pid': self.pid, 
            'title': self.title,
            'price' : self.price,
            'rating' : self.rating,
            'os' : self.os,
            'ram' : self.ram,
            'item_weight' : self.item_weight,
            'product_dimensions' : self.product_dimensions,
            'batteries' : self.batteries,
            'item_model_no' : self.item_model_no,
            'wireless_communication_tech' : self.wireless_communication_tech,
            'connectivity_tech' : self.connectivity_tech,
            'special_features' : self.special_features,
            'display_tech' : self.display_tech,
            'camera_features' : self.camera_features,
            'form_factor' : self.form_factor,
            'color' : self.color,
            'battery_rating' : self.battery_rating,
            'box_contents' : self.box_contents

        }