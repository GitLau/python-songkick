from ..query import SongkickQuery
from .models import SongkickVenue, SongkickEvent


class VenueSearch(SongkickQuery):

    ResponseClass = SongkickVenue
    ResponseEnclosure = 'venue'
    
    def get_api_path(self):
        """Generate the API resource path"""

        return 'search/venues.json'


class VenueEvents(SongkickQuery):

    ResponseClass = SongkickEvent
    ResponseEnclosure = 'event'

    def get_api_path(self):
        """Generate the API resource path"""

        return 'venues/%s/calendar.json' % self._query.pop('venue_id')


class VenueDetails(SongkickQuery):

    ResponseClass = SongkickVenue
    ResponseEnclosure = 'venue'

    def get_api_path(self):
        """Generate the API resource path"""

        return 'venues/%s.json' % self._query.pop('venue_id')

