"""
Open511 Orlando
"""

# library
from flask import jsonify
from flask_restful import Api, Resource
# module
from open511 import app

api = Api(app)

CITY_LIMITS = app.config['CITY_LIMITS']
JURISDICTION = app.config['JURISDICTION']
META = app.config['META']

def format_output(data: dict) -> str:
    """Returns jsonified data with metadata added"""
    data['meta'] = META
    return jsonify(data)

# Static Data Endpoints

class Jurisdiction(Resource):
    def get(self) -> str:
        """Returns jurisdiction data"""
        return format_output({'jurisdiction': JURISDICTION})

class JurisdictionGeography(Resource):
    def get(self) -> str:
        """Returns the city limits as GeoJSON"""
        return format_output({'geography': CITY_LIMITS})

api.add_resource(Jurisdiction, '/jurisdiction')
api.add_resource(JurisdictionGeography, '/jurisdictiongeography')
