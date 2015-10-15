from ..query import SongkickQuery
from .models import SongkickLocation


class LocationQuery(SongkickQuery):
    ResponseClass = SongkickLocation
    ResponseEnclosure = 'location'

    def get_api_path(self):
        "Generate the API resource path"
        return 'search/locations.json'