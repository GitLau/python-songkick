from ..query import SongkickQuery
from .models import SongkickEvent


class MetroAreaCalendar(SongkickQuery):

    ResponseClass = SongkickEvent
    ResponseEnclosure = 'event'
    
    def get_api_path(self):
        """Generate the API resource path"""
        return 'metro_areas/%s/calendar.json' % self._query.pop('metro_area_id')
