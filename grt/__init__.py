from flask import Flask

from grt.config import Development
from grt.ext import migrate, ma, rq
from grt.models import db
from grt.reader import a


def create_app(conf=Development):
    app = Flask(__name__)
    app.config.from_object(conf)
    db.init_app(app)
    rq.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    app.register_blueprint(api)
    return app


from grt.api import api
