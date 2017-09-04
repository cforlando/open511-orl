"""
Open511 Orlando
"""

# stdlib
import json
from multiprocessing import Pool
# library
import requests

LAYERS = [
    'SPECIAL-EVENT',
    'CLOSURE',
    'BLOCKED',
    'DETOUR-N',
    'DETOUR-S',
    'DETOUR-W',
    'DETOUR-E',
    'DETOUR-ARROW',
    'EVENT-STAGING',
    'PROJECT'
]

URL = """http://www2.cityoforlando.net/arcgis/rest/services/Traffic_Control/Road_Closures/MapServer/{}/query?geometry=%7B%0D%0A%22xmin%22%3A+519066.9112086431%2C%0D%0A%22ymin%22%3A+1520502.1260502483%2C%0D%0A%22xmax%22%3A+556428.0223197542%2C%0D%0A%22ymax%22%3A+1541668.7927169148%0D%0A%7D&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelIntersects&returnGeometry=true&returnIdsOnly=false&returnCountOnly=false&returnDistinctValues=false&f=json"""

class GISClient(object):

    layers: (int,) = (1, 2, 3, 4, 5, 6)

    def __init__(self, layers: (int,) = None):
        if not layers is None:
            self.layers = layers

    def fetch_endpoint(self, layer: int):
        """Return data from a single Orlando ArcGIS endpoint by ID"""
        print('fetching', layer)
        data = requests.get(URL.format(layer)).json()['features']
        for item in data:
            item['type'] = LAYERS[layer]
        return data

    def fetch(self):
        """Get all data from the Orlando ArcGIS server"""
        with Pool(3) as pool:
            data = pool.map(self.fetch_endpoint, self.layers)
        # Flatten lists
        return [event for sublist in data for event in sublist]
