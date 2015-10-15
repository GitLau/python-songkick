from ..query import SongkickQuery
from .models import SongkickEvent, SongkickArtist


class ArtistGigographyQuery(SongkickQuery):
    "Gigography-specific query backend"

    ResponseClass = SongkickEvent
    ResponseEnclosure = 'event'

    def get_api_path(self):
        "Generate the API resource path"

        if 'musicbrainz_id' in self._query:
            return 'artists/mbid:%s/gigography.json' % \
                   self._query.pop('musicbrainz_id')
        return 'artists/%s/gigography.json' % \
                self._query.pop('artist_id')


class ArtistCalendar(SongkickQuery):

    ResponseClass = SongkickEvent
    ResponseEnclosure = 'event'

    def get_api_path(self):
        """Generate the API resource path"""
        return 'artists/%s/calendar.json' % self._query.pop('artist_id')


class ArtistSearch(SongkickQuery):

    ResponseClass = SongkickArtist
    ResponseEnclosure = 'artist'

    def get_api_path(self):
        """Generate the API resource path"""
        return 'search/artists.json'


class SimilarArtist(SongkickQuery):

    ResponseClass = SongkickArtist
    ResponseEnclosure = 'artist'

    def get_api_path(self):
        """Generate the API resource path"""
        return 'artists/%s/similar_artists.json' % self._query.pop('artist_id')
