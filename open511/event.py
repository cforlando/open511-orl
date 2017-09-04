"""
Open511 Orlando
"""

# List of attribute keys which correspond to event descriptions
DESC = ('Closure', 'Location')

mapping = (
    ('event_type', 'type'),
    ('geometry', 'geometry')
)

class Event(object):

    def __init__(self, data, source: str = 'cityoforlando.net'):
        self.data = data
        self.source = source

    def dynamic(self) -> dict:
        """Returns dynamic data based on the given data"""
        out = {}
        for outkey, key in mapping:
            if key in self.data:
                out[outkey] = self.data[key]
        # Parse attributes
        if 'attributes' in self.data:
            attrs = self.data['attributes']
            for key in DESC:
                if key in attrs:
                    out['description'] = attrs[key]
        return out

    def static(self) -> dict:
        """Returns static data based on the source"""
        return {
            'jurisdiction_url': f'/jurisdictions/{self.source}',
            'status': 'ACTIVE'
        }

    def export(self) -> {str: object}:
        """Exports the Event in JSON compatible format"""
        return {**self.static(), **self.dynamic()}
