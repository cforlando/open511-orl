"""
Open511 Orlando
"""

# library
from flask import Response, jsonify
from flask_restful import Api, Resource
# module
from open511 import app
from open511.api.validators import BASE_PARSER
from open511.api.dicttoxml import dicttoxml

api = Api(app)

CITY_LIMITS = app.config['CITY_LIMITS']
JURISDICTION = app.config['JURISDICTION']
META = app.config['META']

class Endpoint(Resource):
    """Base Open511 API Endpoint"""

    def output(self, data: dict, args: dict) -> Response:
        """Augment and format output data. Default/catch-all format is JSON"""
        data['meta'] = META
        format = (args['format'] or 'json').lower()
        if format == 'xml':
            response = Response(dicttoxml(data, custom_root='open511orl'))
            response.headers['Content-Type'] = 'application/xml'
        else:
            response = jsonify(data)
        return response

# Static Data Endpoints

class Jurisdiction(Endpoint):
    def get(self) -> str:
        """Returns jurisdiction data"""
        args = BASE_PARSER.parse_args()
        return self.output({'jurisdiction': JURISDICTION}, args)

class JurisdictionGeography(Endpoint):
    def get(self) -> str:
        """Returns the city limits as GeoJSON"""
        args = BASE_PARSER.parse_args()
        return self.output({'geography': CITY_LIMITS}, args)

api.add_resource(Jurisdiction, '/jurisdiction')
api.add_resource(JurisdictionGeography, '/jurisdictiongeography')
