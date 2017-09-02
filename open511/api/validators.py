"""
Open511 Orlando
"""

# stdlib
from copy import copy
# module
from flask_restful.reqparse import RequestParser

BASE_PARSER = RequestParser()
BASE_PARSER.add_argument('format', type=str, help='json (default) or xml')
BASE_PARSER.add_argument('version', type=str, help='Only supports "1.0"')
BASE_PARSER.add_argument('accept-language', type=str, help='Only supports "en"')

PAGINATION_PARSER = copy(BASE_PARSER)
PAGINATION_PARSER.add_argument('limit', type=int, help='Limit the number of returned objects')
PAGINATION_PARSER.add_argument('offset', type=int, help='Offset the starting object')

EVENT_PARSER = copy(PAGINATION_PARSER)
