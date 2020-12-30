from flask_restful import Resource, abort
from flask_restful.reqparse import RequestParser

from grt.models import Region
from grt.schema import RegionSchema

parser = RequestParser(trim=True, bundle_errors=True)


class RegionRes(Resource):
    def get(self):
        parser.add_argument('name', location='args', required=False)
        args = parser.parse_args()
        if not args.get('name'):
            region = Region.query.all()
            data = RegionSchema()
            return data.dump(region, many=True)
        else:
            region = Region.query.filter(Region.name == args.get('name').lower()).first_or_404()
            data = RegionSchema()
            return data.dump(region)

    def post(self):
        parser.add_argument('name', required=True, location='json', type=str)
        args = parser.parse_args()
        region = Region.query.filter(Region.name == args.name).first_or_404()
        if region:
            return abort(409)
        region = Region(name=args.name)
        return region.save()

    def put(self):
        parser.add_argument('id', location='args', type=int, required=False)
        parser.add_argument('name', location='args', type=int, required=False)
        args = parser.parse_args()
        region = Region.query.get_or_404(args.id)
        if Region.query.filter(Region.id != region.id, Region.name == args.name).first():
            return abort(409)
        region.name = args.name
        return region.save()

    def delete(self):
        parser.add_argument('id', location='args', type=int, required=False)
        args = parser.parse_args()
        region = Region.query.get_or_404(args.id)
        return region.delete()
