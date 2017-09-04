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

ROOT_DATA = {
    'jurisdictions': [
        {
            'id': 'cityoforlando.net',
            'name': 'Orlando',
            'url': BASEURL + 'jurisdiction/cityoforlando.net',
            'geography_url': BASEURL + 'jurisdiction/cityoforlando.net/geography'
        }
    ],
    'services' : [
        {
            'service_type_url': 'http://open511.org/services/events',
            'url' : '/events/'
        },
        {
            'service_type_url': 'http://open511.org/services/events',
            'url' : '/areas/'
        }
    ]
}

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

GEOMETRIES = {g[0]: load(open(os.path.join(BASEDIR, 'geometries', g[1]))) for g in (
    ('cityoforlando.net', 'orlando.geojson'),
)}
