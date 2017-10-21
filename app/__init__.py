from flask import Flask
from flask_bootstrap import Bootstrap

from config import config_options

bootstrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)

    # configuring the app
    app.config.from_object(config_options[config_name])

    # initializing flak extensions
    bootstrap.init_app(app)

    # registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting up configurations
    from .requests import configure_request
    configure_request(app)


    return app