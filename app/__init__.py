from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config_options

bootstrap = Bootstrap()

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)

    # configuring the app
    app.config.from_object(config_options[config_name])

    # initializing flak extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # registering auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # setting up configurations
    from .requests import configure_request
    configure_request(app)


    return app