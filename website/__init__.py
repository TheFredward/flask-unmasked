from flask import Flask


def create_app():
    # Import views.py and set up pages from blueprint
    # Insert database here if using one
    app = Flask(__name__)

    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app


