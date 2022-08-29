from flask import Flask, render_template
from dotenv import load_dotenv
from os import device_encoding, environ

from routes import views
from repository import db
from repository.user import create_admin_user
from routes.admin import admin
from service.auth import login_manager
from service.cache import cache
load_dotenv()

def create_app():
    app = Flask(__name__, static_url_path='/assets', static_folder='assets', template_folder='templates')

    app.config.from_object(environ['CONFIGURATION_SETUP'])

    initialize_app(app)

    return app


def initialize_app(app):
    app.register_blueprint(views)
    db.init_app(app)
    try:
        db.create_all(app=app)
    except:
        app.logger.warning("Database CREATE ALL Failed")

    try:
        create_admin_user(app)
    except:
        app.logger.warning("Admin Creation Failed")

    login_manager.init_app(app)

    admin.init_app(app)

    cache.init_app(app)

    app.register_error_handler(404, page_not_found)


def page_not_found(error):
    return render_template('/errors/404.html', title = '404'), 404

app = create_app()

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)