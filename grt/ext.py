from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_rq2 import RQ
from flask_sqlalchemy import SQLAlchemy

rq = RQ()
migrate = Migrate()
db = SQLAlchemy()
ma = Marshmallow()
