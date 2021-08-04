from flask import Flask
from flask_redis import Redis
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from flask_assets import Environment

redis = Redis()
mysql = MySQL(cursorclass=DictCursor)


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile('config.py')

    assets = Environment()

    style_bundle.build()
    js_bundle.build()

    mysql.init_app(app)
    redis.init_app(app)
    assets.init_app(app)

    with app.app_context():
        from .home import routes

        app.register_blueprint(routes.home_bp)

        return app




