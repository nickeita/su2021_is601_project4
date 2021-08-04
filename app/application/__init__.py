from flask import Flask
from flask_redis import Redis
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy

agent_db = SQLAlchemy()
houses_db = SQLAlchemy()

redis = Redis()


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile('config.py')

    assets = Environment()

    style_bundle.build()
    js_bundle.build()

    agent_db.init_app(app)
    houses_db.init_app(app)
    redis.init_app(app)
    assets.init_app(app)

    with app.app_context():
        from .home import routes
        from .agent import routes

        app.register_blueprint(routes.home_bp)

        return app




