from flask import Flask
from flask_redis import Redis
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

redis = Redis()
mysql = MySQL(cursorclass=DictCursor)


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile('config.py')

    mysql.init_app(app)
    redis.init_app(app)

    with app.app_context():
        from .home import routes

        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(admin.admin_bp)

        return app




