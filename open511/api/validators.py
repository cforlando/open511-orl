"""
Open511 Orlando
"""

from flask_restful.reqparse import RequestParser

BASE_PARSER = RequestParser()
BASE_PARSER.add_argument('format', type=str, help='json (default) or xml')
BASE_PARSER.add_argument('version', type=str, help='Only supports "1.0"')
BASE_PARSER.add_argument('accept-language', type=str, help='Only supports "en"')
