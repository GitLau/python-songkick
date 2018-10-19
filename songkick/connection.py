import urllib
#import urlparse

import httplib2
import warnings

from .events.query import EventQuery
from .artists.query import ArtistGigographyQuery, ArtistCalendar, ArtistSearch, SimilarArtist
from .users.query import UserGigographyQuery
from .locations.query import LocationQuery
from .exceptions import SongkickRequestError
from .setlists.query import SetlistQuery
from .venues.query import VenueSearch, VenueEvents, VenueDetails
from .metro_areas.query import MetroAreaCalendar


class SongkickConnection(object):

    ApiBase = 'http://api.songkick.com/api/3.0/'
    
    def __init__(self, api_key):
        self.api_key = api_key
        self._http = httplib2.Http('.songkick_cache')

    def make_request(self, url, method='GET', body=None, headers=None):
        """Make an HTTP request.

        This could stand to be a little more robust, but Songkick's API
        is very straight-forward: 200 is a success, anything else is wrong.
        """

        headers = headers or {}
        headers['Accept-Charset'] = 'utf-8'

        response, content = self._http.request(url, method, body, headers)

        if int(response.status) != 200:
            raise SongkickRequestError('Could not load %s: [%s] %s' %
                                       (url, response.status,
                                        response.reason))
        return content

    def build_songkick_url(self, api_path, request_args):
        "Assemble the Songkick URL"

        # insert API key
        request_args['apikey'] = self.api_key

        # construct the complete api resource url, minus args
        url = urllib.parse.urljoin(SongkickConnection.ApiBase, api_path)

        # break down the url into its components, inject args
        # as query string and recombine the url
        url_parts = list(urllib.parse.urlparse(url))
        url_parts[4] = urllib.parse.urlencode(request_args)
        url = urllib.parse.urlunparse(url_parts)
        
        return url

    # Venues
    @property
    def venue_search(self):
        return VenueSearch(self)

    @property
    def venue_details(self):
        return VenueDetails(self)

    @property
    def venue_events(self):
        return VenueEvents(self)

    # Metro Areas
    @property
    def metro_area_events(self):
        return MetroAreaCalendar(self)

    # Events
    @property
    def event_search(self):
        return EventQuery(self)

    @property
    def event_setlists(self):
        return SetlistQuery(self)

    # Users
    @property
    def user_gigography(self):
        return UserGigographyQuery(self)

    # Artists
    @property
    def artist_gigography(self):
        return ArtistGigographyQuery(self)

    @property
    def artist_events(self):
        return ArtistCalendar(self)

    @property
    def artist_search(self):
        return ArtistSearch(self)

    @property
    def artists_similar(self):
        return SimilarArtist(self)

    # Locations
    @property
    def artists_similar(self):
        return LocationQuery(self)

    # Deprecated
    @property
    def events(self):
        warnings.warn("deprecated", DeprecationWarning)
        return EventQuery(self)

    @property
    def gigography(self):
        warnings.warn("deprecated", DeprecationWarning)
        return ArtistGigographyQuery(self)

    @property
    def setlists(self):
        warnings.warn("deprecated", DeprecationWarning)
        return SetlistQuery(self)


