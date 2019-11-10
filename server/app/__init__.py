from flask import Flask
def create_app():
    app = Flask(__name__)
    from app.resultpage.resultpage import result
    from app.aboutpage.about import about
    from app.buypage.buy import buy
    from app.cartpage.cart import cart
    from app.homepage.home import home
    app.register_blueprint(result)
    app.register_blueprint(about)
    app.register_blueprint(buy)
    app.register_blueprint(cart)
    app.register_blueprint(home)
    return app
    