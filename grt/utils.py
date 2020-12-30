from flask_restful import abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from grt.ext import db


class ActiveRecord:
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            return abort(500)

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            return abort(500)
