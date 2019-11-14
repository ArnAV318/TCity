from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#from flask_mail import Mail
from app.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'loginpage.loginpage'
#login_manager.login_message_category = 'info'


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    #mail.init_app(app)

    from app.resultpage.resultpage import result
    from app.aboutpage.about import about
    from app.buypage.buy import buy
    from app.cartpage.cart import cart
    from app.homepage.home import home
    from app.inputdata.inputdata import input
    from app.login.login import login
    app.register_blueprint(result)
    app.register_blueprint(about)
    app.register_blueprint(buy)
    app.register_blueprint(cart)
    app.register_blueprint(home)
    app.register_blueprint(input)
    app.register_blueprint(login)
    return app
    