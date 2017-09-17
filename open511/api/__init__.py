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

DEFAULT_ARGS = app.config['DEFAULT_ARGS']
BASEURL = app.config['BASEURL']

GEOMETRIES = app.config['GEOMETRIES']
JURISDICTIONS = app.config['JURISDICTIONS']
META = app.config['META']
SERVICES = app.config['SERVICES']

CITY_IDS = list(GEOMETRIES.keys())

class Endpoint(Resource):
    """Base Open511 API Endpoint"""

    validator: 'RequestParser' = BASE_PARSER

    @staticmethod
    def validate_city_id(id: str):
        """Aborts the request if the city ID is not accepted"""
        if not id in CITY_IDS:
            abort(400, message='Not a recognized city ID')

    @staticmethod
    def is_accepted_format(format: str) -> bool:
        """Returns True if the server can return the requested format"""
        return format is None or format.lower() in ('json', 'xml')

    def get_args(self) -> {str: object}:
        """Get request args for a given parser after passing initial checks"""
        args = self.validator.parse_args()
        if not self.is_accepted_format(args['format']):
            abort(406, message='The server cannot return the data in the requested format')
        for key, value in args.items():
            if value is None and key in DEFAULT_ARGS:
                args[key] = DEFAULT_ARGS[key]
        return args

    @staticmethod
    def make_pagination(url: str, limit: int, offset: int) -> {str: object}:
        """Returns the pagination response element"""
        return {
            'next_url': url + f'?limit={limit}&offset={limit + offset}',
            'offset': offset
        }

    def output(self, data: dict, args: dict, page_url: str = None) -> Response:
        """Augment and format output data. Default/catch-all format is JSON
        Will add pagination data if given a URL for page_url
        """
        data['meta'] = META
        if page_url:
            data['pagination'] = self.make_pagination(page_url, args['limit'], args['offset'])
        if args['format'] == 'xml':
            response = Response(dicttoxml(data, custom_root='open511orl'))
            response.headers['Content-Type'] = 'application/xml'
        else:  # JSON catch-all
            response = jsonify(data)
        return response

# Static Data Endpoints

class Root(Endpoint):

    @staticmethod
    def condense(jurisdiction: dict):
        """Returns the jurisdiction dict containing only id, name, url, and geography_url"""
        return {
            'id': jurisdiction['id'],
            'name': jurisdiction['name'],
            'url': BASEURL + jurisdiction['url'],
            'geography_url': BASEURL + jurisdiction['geography_url']
        }

    def get(self) -> Response:
        """Returns the server root/discovery data"""
        data = {
            'jurisditions': [self.condense(j) for j in JURISDICTIONS],
            'services': SERVICES
        }
        return self.output(data, self.get_args())

class Jurisdiction(Endpoint):
    def get(self) -> Response:
        """Returns all jurisdiction data"""
        return self.output({'jurisdictions': JURISDICTIONS}, self.get_args())

class JurisdictionID(Endpoint):
    def get(self, id: str) -> Response:
        """Returns all jurisdiction data"""
        self.validate_city_id(id)
        data = {'jurisdiction': j for j in JURISDICTIONS if j['id'] == id}
        return self.output(data, self.get_args())

class GeographyID(Endpoint):
    def get(self, id: str) -> Response:
        """Returns the city limits as GeoJSON"""
        self.validate_city_id(id)
        args = self.get_args()
        return self.output({'geography': GEOMETRIES[id]}, args)

api.add_resource(Root, '/')
api.add_resource(Jurisdiction, '/jurisdictions')
api.add_resource(JurisdictionID, '/jurisdictions/<string:id>')
api.add_resource(GeographyID, '/jurisdictions/<string:id>/geography')

import open511.api.events
