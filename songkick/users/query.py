from ..query import SongkickQuery
from .models import SongkickEvent


class UserGigographyQuery(SongkickQuery):
    "Gigography-specific query backend"

    ResponseClass = SongkickEvent
    ResponseEnclosure = 'event'

    def get_api_path(self):
        "Generate the API resource path"
        return 'users/%s/gigography.json' % \
                self._query.pop('username')


# SOMEONE PLEASE FINISH MY MODEL!!!
# "calendarEntry": [
#           {"reason": {
#               "trackedArtist": [ARTIST, ARTIST],
#               "attendance": "i_might_go|im_going”
#            },
#            "event": {EVENT}
#           }]

# @todo later open source community!!!!
class ArtistCalendar(SongkickQuery):

    ResponseClass = SongkickEvent
    ResponseEnclosure = 'event'

    def get_api_path(self):
        """Generate the API resource path"""
        return 'artists/%s/calendar.json' % self._query.pop('artist_id')