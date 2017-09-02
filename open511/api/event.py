"""
Open511 Orlando
"""

from open511.api import api, Endpoint
from open511.api.validators import EVENT_PARSER

class Event(object):

    def __init__(self, data):
        self.data = data

    def json(self) -> {str: object}:
        """Returns the Event in JSON format"""
        return {'test': True, 'value': self.data}

class EventEndpoint(Endpoint):

    parser = EVENT_PARSER
    url = '/events'

    @staticmethod
    def get_events(start, stop):
        return [Event(i) for i in range(start, stop)]

    def get(self):
        """Return all events"""
        args = self.get_args()
        limit, offset = args['limit'], args['offset']
        data = {'events': [event.json() for event in self.get_events(offset, limit + offset)]}
        return self.output(data, args, self.url)

class EventByJurisdiction(EventEndpoint):

    url = '/events/{}'

    def get(self, id: str) -> 'Response':
        """Return all events for a jurisdiction ID"""
        self.validate_city_id(id)
        args = self.get_args()
        limit, offset = args['limit'], args['offset']
        data = {'events': [event.json() for event in self.get_events(offset, limit + offset)]}
        return self.output(data, args, self.url.format(id))

class EventByID(EventEndpoint):

    url = '/events/{}/{}'

    def get(self, id: str, eid: int) -> 'Response':
        """Return a single event by ID for a jurisdiction ID"""
        self.validate_city_id(id)
        args = self.get_args()
        limit, offset = args['limit'], args['offset']
        data = {'events': [event.json() for event in self.get_events(offset, limit + offset)]}
        return self.output(data, args, self.url.format(id, eid))

# Add endpoints using constructed URLs
for cls, vals in ((EventEndpoint, tuple()),
                  (EventByJurisdiction, ('<id>',)),
                  (EventByID, ('<id>', '<int:eid>'))):
    api.add_resource(cls, cls.url.format(*vals))
