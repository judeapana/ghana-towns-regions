from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from grt.models import Town
from grt.schema import TownSchemaType

parser = RequestParser(bundle_errors=True, trim=True)


class TownRes(Resource):
    def get(self):
        parser.add_argument('name', required=True, location='args')
        args = parser.parse_args()
        town = Town.query.filter(Town.name == args.name).all()
        data = TownSchemaType()
        return data.dump(town, many=True)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
