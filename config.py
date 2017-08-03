"""
Michael duPont - michael@mdupont.com
config.py - Holds the high-level settings for the web app
"""

# stdlib
import os
from json import load

BASEDIR = os.path.abspath(os.path.dirname(__file__))

META = {
    'version': 'v1'
}

JURISDICTION = {
    'id': 'cityoforlando.net',
    'name': 'Orlando',
    'url': '/jurisdiction',
    'description': 'Road closure information from Orlando, FL',
    'geography_url': '/jurisdictiongeo',
    'languages': [
        'en'
    ],
    'phone': '123-456-7890',
    'license_url': 'http://www.cityoforlando.net/legal/',
    'timezone': 'America/New_York',
    'email': 'test@cityoforlando.net'
}

CITY_LIMITS = load(open(os.path.join(BASEDIR, 'orlando.geojson')))
