"""
Open511 Orlando
"""

# library
from dicttoxml import dicttoxml
from flask import Response, jsonify
from flask_restful import Api, Resource, abort
# module
from open511 import app
from open511.api.validators import BASE_PARSER

api = Api(app)

GEOMETRIES = app.config['GEOMETRIES']
JURISDICTIONS = app.config['JURISDICTIONS']
META = app.config['META']
ROOT_DATA = app.config['ROOT_DATA']

CITY_IDS = list(GEOMETRIES.keys())

class Endpoint(Resource):
    """Base Open511 API Endpoint"""

    @staticmethod
    def validate_city_id(id: str):
        """Aborts the request if the city ID is not accepted"""
        if not id in CITY_IDS:
            abort(400, message='Not a recognized city ID')

    @staticmethod
    def is_accepted_format(format: str) -> bool:
        """Returns True if the server can return the requested format"""
        return format is None or format.lower() in ('json', 'xml')

    def get_args(self, parser: 'RequestParser') -> dict:
        """Get request args for a given parser after passing initial checks"""
        args = parser.parse_args()
        if not self.is_accepted_format(args['format']):
            abort(406, message='The server cannot return the data in the requested format')
        return args

    def output(self, data: dict, args: dict) -> Response:
        """Augment and format output data. Default/catch-all format is JSON"""
        data['meta'] = META
        if format == 'xml':
            response = Response(dicttoxml(data, custom_root='open511orl'))
            response.headers['Content-Type'] = 'application/xml'
        else:  # JSON catch-all
            response = jsonify(data)
        return response

# Static Data Endpoints

class Root(Endpoint):
    def get(self) -> Response:
        """Returns the server root/discovery data"""
        args = self.get_args(BASE_PARSER)
        return self.output(ROOT_DATA, args)

class Jurisdiction(Endpoint):
    def get(self) -> Response:
        """Returns all jurisdiction data"""
        args = self.get_args(BASE_PARSER)
        return self.output({'jurisdictions': JURISDICTIONS}, args)

class JurisdictionID(Endpoint):
    def get(self, id: str) -> Response:
        """Returns all jurisdiction data"""
        self.validate_city_id(id)
        args = self.get_args(BASE_PARSER)
        return self.output({'jurisdiction': j for j in JURISDICTIONS if j['id'] == id}, args)

class GeographyID(Endpoint):
    def get(self, id: str) -> Response:
        """Returns the city limits as GeoJSON"""
        self.validate_city_id(id)
        args = self.get_args(BASE_PARSER)
        return self.output({'geography': GEOMETRIES[id]}, args)

api.add_resource(Root, '/')
api.add_resource(Jurisdiction, '/jurisdictions')
api.add_resource(JurisdictionID, '/jurisdictions/<string:id>')
api.add_resource(GeographyID, '/jurisdictions/<string:id>/geography')
