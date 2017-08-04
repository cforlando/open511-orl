"""
Open511 Orlando
"""

from flask_restful.reqparse import RequestParser

BASE_PARSER = RequestParser()
BASE_PARSER.add_argument('format', type=str, help='json (default) or xml')
