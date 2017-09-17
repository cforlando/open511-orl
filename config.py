"""
Michael duPont - michael@mdupont.com
config.py - Holds the high-level settings for the web app
"""

# stdlib
import os
from json import load

BASEDIR = os.path.abspath(os.path.dirname(__file__))
BASEURL = 'http://open511.cityoforlando.net/'

# Default parameter arguements for all endpoints
# Parameter names are unique across all endpoints
# Parameters are filtered based on the endpoint's validator

DEFAULT_ARGS = {
    'limit': 20,
    'offset': 0
}

META = {
    'version': 'v1'
}

# Services shown on root

SERVICES = [
    {
        'service_type_url': 'http://open511.org/services/events',
        'url' : '/events/'
    },
    {
        'service_type_url': 'http://open511.org/services/areas',
        'url' : '/areas/'
    }
]

# List of jurisdiction information

JURISDICTIONS = [
    {
        'id': 'cityoforlando.net',
        'name': 'Orlando',
        'url': '/jurisdictions/cityoforlando.net',
        'description': 'Road closure information from Orlando, FL',
        'geography_url': '/jurisdictions/cityoforlando.net/geography',
        'languages': [
            'en'
        ],
        'phone': '123-456-7890',
        'license_url': 'http://www.cityoforlando.net/legal/',
        'timezone': 'America/New_York',
        'email': 'test@cityoforlando.net'
    }
]

# This creates a dictionary associating a jurisdiction ID with its GeoJSON
#
# To add a new entry, put the GeoJSON file in the geometries folder and
# add a new tuple below with the jurisdiction ID and name of the file

GEOMETRIES = {g[0]: load(open(os.path.join(BASEDIR, 'geometries', g[1]))) for g in (
    ('cityoforlando.net', 'orlando.geojson'),
)}
