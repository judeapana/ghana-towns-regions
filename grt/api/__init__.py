from flask import Blueprint
from flask_restful import Api

from grt.api.market_day import MarketDayRes
from grt.api.region import RegionRes
from grt.api.town import TownRes

api = Blueprint('api', __name__, url_prefix='/api')
xapi = Api(api)

xapi.add_resource(RegionRes, '/region')
xapi.add_resource(TownRes, '/town')
xapi.add_resource(MarketDayRes, '/market-day')
