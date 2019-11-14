from app import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(uid):
    return user.query.get(int(uid))

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
    product_type = db.Column(db.String(30))
    pieces = db.Column(db.Integer())





    def __init__(self, title, price, rating, os, ram, item_weight, product_dimensions, batteries, item_model_no, wireless_communication_tech, connectivity_tech, special_features, display_tech, camera_features, form_factor, color, battery_rating, box_contents,product_type,pieces):
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
        self.product_type = product_type
        self.pieces = pieces
    

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

class user(db.Model , UserMixin):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    password = db.Column(db.String(100))

    def __repr__(self):
        return '<id {} name {}>'.format(self.uid,self.name)

    def get_id(self):
        return self.uid

    def __init__(self, name,email,address,password):
        self.name = name
        self.email = email
        self.address = address
        self.password = password

    def serialize(self):
        return {
            'uid' : self.uid,
            'name' : self.name,
            'email' : self.email,
            'address' : self.address,
            'password' : self.password
        }

class Tv_product(db.Model):
    __tablename__ = 'tv_product'
    
    pid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    price = db.Column(db.Integer())
    rating = db.Column(db.Float())
    Brand = db.Column(db.String(100))
    Model = db.Column(db.String(100))
    Model_Name = db.Column(db.String(100))
    Model_Year = db.Column(db.String(100))
    Item_Weight = db.Column(db.String(100))
    Product_Dimensions = db.Column(db.String(100))
    Item_model_number = db.Column(db.String(100))
    Processor_Speed = db.Column(db.String(100))
    Response_Time = db.Column(db.String(100))
    Resolution = db.Column(db.String(100))
    Compatible_Devices = db.Column(db.String(100))
    Additional_Features = db.Column(db.String(200))
    Included_Components = db.Column(db.String(200))
    Number_Of_Items = db.Column(db.String(100))
    Display_Technology = db.Column(db.String(100))
    Screen_Size = db.Column(db.String(100))
    Display_Type = db.Column(db.String(100))
    Image_Aspect_Ratio = db.Column(db.String(100))
    Image_Contrast_Ratio = db.Column(db.String(100))
    Display_Resolution_Maximum = db.Column(db.String(100))
    Audio_Features_Description = db.Column(db.String(100))
    Supported_Audio_Format = db.Column(db.String(50))
    product_type = db.Column(db.String(100))
    pieces = db.Column(db.Integer())

    def __init__(self, title, price, rating,Brand,Model,Model_Name,Model_Year,Item_Weight,Product_Dimensions,Item_model_number,Processor_Speed,Response_Time,Resolution,Compatible_Devices,Additional_Features,Included_Components,Number_Of_Items,Display_Technology,Screen_Size,Display_Type,Image_Aspect_Ratio,Image_Contrast_Ratio,Display_Resolution_Maximum,Audio_Features_Description,Supported_Audio_Format,product_type,pieces):
        self.title = title
        self.price = price
        self.rating = rating
        self.Brand = Brand
        self.Model = Model
        self.Model_Name = Model_Name
        self.Model_Year = Model_Year
        self.Item_Weight = Item_Weight
        self.Product_Dimensions = Product_Dimensions
        self.Item_model_number = Item_model_number
        self.Processor_Speed = Processor_Speed
        self.Response_Time = Response_Time
        self.Resolution = Resolution
        self.Compatible_Devices = Compatible_Devices
        self.Additional_Features = Additional_Features
        self.Included_Components = Included_Components
        self.Number_Of_Items = Number_Of_Items
        self.Display_Technology = Display_Technology
        self.Screen_Size = Screen_Size
        self.Display_Type = Display_Type
        self.Image_Aspect_Ratio = Image_Aspect_Ratio
        self.Image_Contrast_Ratio = Image_Contrast_Ratio
        self.Display_Resolution_Maximum = Display_Resolution_Maximum
        self.Audio_Features_Description = Audio_Features_Description
        self.Supported_Audio_Format = Supported_Audio_Format
        self.product_type = product_type
        self.pieces = pieces
        
    
    def __repr__(self):
        return '<id {} name {}>'.format(self.pid,self.title)

    def serialize(self):
        return {
            'pid': self.pid,
            'title':self.title,
            'price':self.price,
            'rating':self.rating,
            'Brand' : self.brand,
            'Model' :self.Model,
            'Model Name' : self.Model_Name,
            'Model Year' : self.Model_Year,
            'Item Weight' : self.Item_Weight,
            'Product Dimensions' : self.Product_Dimensions,
            'Item model number' : self.Item_model_number,
            'Processor Speed' : self.Processor_Speed,
            'Response Time' : self.Response_Time,
            'Resolution' : self.Resolution,
            'Compatible Devices' : self.Compatible_Devices,
            'Additional Features' : self.Additional_Features,
            'Included Components' : self.Included_Components,
            'Number Of Items' : self.Number_Of_Items,
            'Display Technology' : self.Display_Technology,
            'Screen Size' : self.Screen_Size,
            'Display Type' : self.Display_Type,
            'Image Aspect Ratio' : self.Image_Aspect_Ratio,
            'Image Contrast Ratio' : self.Image_Contrast_Ratio,
            'Display Resolution Maximum' : self.Display_Resolution_Maximum,
            'Audio Features Description' : self.Audio_Features_Description,
            'Supported Audio Format' : self.Supported_Audio_Format,
            'product_type' : self.product_type,
            'pieces' : self.pieces
        }

class Fridge_product(db.Model):
    __tablename__ = 'fridge_product'

    pid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    price = db.Column(db.Integer())
    rating = db.Column(db.Float())
    Brand = db.Column(db.String(100))
    Model = db.Column(db.String(100))
    Energy_Efficiency = db.Column(db.String(100))
    Capacity = db.Column(db.String(100))
    Installation_Type = db.Column(db.String(100))
    Form_Factor = db.Column(db.String(100))
    Colour = db.Column(db.String(100))
    Voltage = db.Column(db.String(100))
    Defrost_System = db.Column(db.String(100))
    Shelf_Type = db.Column(db.String(100))
    Material = db.Column(db.String(100))
    Included_Components = db.Column(db.String(200))
    Batteries_Included = db.Column(db.String(100))
    Batteries_Required = db.Column(db.String(100))
    product_type = db.Column(db.String(30))
    pieces = db.Column(db.Integer())

    def __repr__(self):
        return '<id {} name {}>'.format(self.pid,self.title)

    def __init__(self, title, price, rating,Brand,Model,Energy_Efficiency,Capacity,Installation_Type,Form_Factor,Colour,Voltage,DefrostSystem,Shelf_Type,Material,Included_Components,Batteries_Included,Batteries_Required):
        self.title = title
        self.price = price
        self.rating = rating
        self.Brand = Brand
        self.Model = Model
        self.Energy_Efficiency = Energy_Efficiency
        self.Capacity = Capacity
        self.Installation_Type = Installation_Type
        self.Form_Factor = Form_Factor
        self.Colour = Colour
        self.Voltage = Voltage
        self.Defrost_System = DefrostSystem
        self.Shelf_Type = Shelf_Type
        self.Material = Material
        self.Included_Components = Included_Components
        self.Batteries_Included = Batteries_Included
        self.Batteries_Required = Batteries_Required


    def serialize(self):
        return {
            'pid': self.pid,
            'title':self.title,
            'price':self.price,
            'rating':self.rating,
            "Brand" : self.Brand,
            "Model" : self.Model,
            "Energy Efficiency" : self.Energy_Efficiency,
            "Capacity" : self.Capacity,
            "Installation Type" : self.Installation_Type,
            "Form Factor" : self.Form_Factor,
            "Colour" : self.Color,
            "Voltage" : self.Volatge,
            "Defrost System" : self.Defrost_System,
            "Shelf Type": self.Shelf_Type,
            "Material" : self.Material,
            "Included Components" : self.Included_Components,
            "Batteries Included" : self.Batteries_Included,
            "Batteries Required" : self.Batteries_Required,
            'product_type' : self.product_type,
            'pieces' : self.pieces

        }

class image_model(db.Model):
    __tablename__ = 'image_model'
    pid = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(100))
    path = db.Column(db.String(300))

    def __repr__(self):
        return '<id {} name {}>'.format(self.pid,self.id)
    def __serialize__():
        return {
            'pid' : self.pid,
            'id':self.id,
            'product_type':self.product_type,
            'path':self.path
        }
    def __init__(self,pid,product_type,path)    :
        self.pid=pid
        self.path=path
        self.product_type=product_type

