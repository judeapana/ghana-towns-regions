from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from grt.models import MarketDay
from grt.schema import MarketDaySchema

parser = RequestParser(bundle_errors=True, trim=True)


class MarketDayRes(Resource):
    def get(self):
        parser.add_argument('town', location='args', type=str, required=True)
        args = parser.parse_args()
        data = MarketDaySchema()
        market = MarketDay.query.filter(MarketDay.town.has(name=args.town)).all()
        return data.dump(market, many=True)
