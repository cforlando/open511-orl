"""
Open511 Orlando
"""

from open511.api import api, Endpoint
from open511.api.validators import EVENT_PARSER
from open511.client import GISClient
from open511.event import Event

class EventEndpoint(Endpoint):

    validator: 'RequestParser' = EVENT_PARSER
    url: str = '/events'

    @staticmethod
    def get_events(start, stop) -> [Event]:
        """Return a list of initialized Events fetched from the Orlando ArcGIS server"""
        client = GISClient()
        data = client.fetch()
        if start > len(data):
            return []
        elif stop > len(data):
            data = data[start:]
        else:
            data = data[start: stop]
        return [Event(event) for event in data]

    def get(self):
        """Return all events"""
        args = self.get_args()
        limit, offset = args['limit'], args['offset']
        data = {'events': [event.export() for event in self.get_events(offset, limit + offset)]}
        return self.output(data, args, self.url)

class EventByJurisdiction(EventEndpoint):

    url = '/events/{}'

    def get(self, id: str) -> 'Response':
        """Return all events for a jurisdiction ID"""
        self.validate_city_id(id)
        args = self.get_args()
        limit, offset = args['limit'], args['offset']
        data = {'events': [event.export() for event in self.get_events(offset, limit + offset)]}
        return self.output(data, args, self.url.format(id))

# class EventByID(EventEndpoint):

#     url = '/events/{}/{}'

#     def get(self, id: str, eid: int) -> 'Response':
#         """Return a single event by ID for a jurisdiction ID"""
#         self.validate_city_id(id)
#         args = self.get_args()
#         limit, offset = args['limit'], args['offset']
#         data = {'events': [event.json() for event in self.get_events(offset, limit + offset)]}
#         return self.output(data, args, self.url.format(id, eid))

# Add endpoints using constructed URLs
for cls, vals in ((EventEndpoint, tuple()),
                  (EventByJurisdiction, ('<id>',))
                  #(EventByID, ('<id>', '<int:eid>'))
                  ):
    api.add_resource(cls, cls.url.format(*vals))
