from flask import Flask
def create_app():
    app = Flask(__name__)
    from app.resultpage.resultpage import result
    app.register_blueprint(result)
    return app
    