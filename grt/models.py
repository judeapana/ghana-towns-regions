import datetime

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_utils import Timestamp

from grt.ext import db
from grt.utils import ActiveRecord


class Region(db.Model, Timestamp, ActiveRecord):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    towns = db.relationship('Town', backref=db.backref('region'), cascade='all,delete,delete-orphan',
                            lazy='dynamic')


class Town(db.Model, Timestamp, ActiveRecord):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id', ondelete='cascade'), nullable=False)
    market_days = db.relationship('MarketDay', backref=db.backref('town'), cascade='all,delete,delete-orphan',
                                  lazy='dynamic')


class MarketDay(db.Model, Timestamp, ActiveRecord):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    recent_day = db.Column(db.DateTime, nullable=False)
    interval = db.Column(db.Integer, nullable=False)
    town_id = db.Column(db.Integer, db.ForeignKey('town.id', ondelete='cascade'), unique=True, nullable=False)

    @hybrid_property
    def day(self):
        return datetime.datetime.utcnow() + (
                self.recent_day - datetime.datetime.utcnow() + datetime.timedelta(days=self.interval))
