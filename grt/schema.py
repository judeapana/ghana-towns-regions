from flask_marshmallow.fields import fields as f

from grt.ext import ma
from grt.models import Town, Region, MarketDay


class RegionSchemaType(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Region
        fields = ('name',)


class TownSchemaType(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Town
        fields = ('region', 'town')

    town = f.Function(lambda x: x.name)
    region = f.Nested(RegionSchemaType)


class TownSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Town
        fields = ('name',)


class RegionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Region
        fields = ('region', 'towns')

    region = f.Function(lambda x: x.name)
    towns = f.Function(lambda x: [i.name for i in x.towns.all()])


class MarketDaySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MarketDay
        fields = ['interval', 'day', 'town']

    town = f.Nested(TownSchema)
    day = f.Function(lambda x: x.day.strftime('%d %B %Y'))
