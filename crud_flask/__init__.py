from dynaconf import FlaskDynaconf
from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from crud_flask.models import db
from crud_flask.views import create_user, delete_user, detail_user, home, update_user

migrate = Migrate()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)

    FlaskDynaconf(app, envvar_prefix="FLASK", settings_files=["settings.toml"])

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    home.init_app(app)
    create_user.init_app(app)
    delete_user.init_app(app)
    update_user.init_app(app)
    detail_user.init_app(app)

    return app
