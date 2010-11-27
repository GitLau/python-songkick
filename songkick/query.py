import json
from math import ceil

from songkick.exceptions import SongkickDecodeError


class SongkickResultPage(object):

    def __init__(self, result_class, object_list, object_count, 
                 per_page, page_number):
        self._result_class = result_class
        self.object_list = object_list or []
        self.page_number = page_number
        self.page_count = int(ceil(float(object_count) / int(per_page)))
        self.object_count = object_count

    def __iter__(self):
        for obj in self.object_list:
            yield self._result_class._from_json(obj)

    def next_page_number(self):
        return self.page_number + 1

    def previous_page_number(self):
        return self.page_number - 1

    def has_next(self):
        return self.page_number < self.paginator.page_count

    def has_previous(self):
        return self.page_number > 1


class SongkickQuerySet(object):

    def __init__(self, connection):
        self._query = {}
        self._result_cache = None
        self._connection = connection

    @classmethod
    def _parse_response(cls, event_data):
        "Parse event data, return ``SongkickResultPage``."
        
        try:
            data = json.loads(event_data)
        except Exception, exc:
            msg = "Couldn't decode response: %s" % exc
            raise SongkickDecodeError(msg)

        # parse results
        page = data['resultsPage']
        page_number = page.get('page')
        per_page = page.get('perPage', 50)
        total_entries = page.get('totalEntries', 0)
        results_wrapper = page.get('results')

        if not cls.RESPONSE_ENCLOSURE in results_wrapper:
            raise SongkickDecodeError("%s not found in results page." % \
                                          cls.RESPONSE_ENCLOSURE)
        object_list = results_wrapper.get(cls.RESPONSE_ENCLOSURE)

        # generate page of results
        return SongkickResultPage(object_list=object_list,
                                  object_count = total_entries,
                                  result_class=cls.RESPONSE_CLASS,
                                  page_number=page_number,
                                  per_page=per_page)

    def _get_api_path(self):        
        raise NotImplementedError

    def query(self, **query_kwargs):
        "Query Songkick"

        # update query args
        self._query = query_kwargs

        # generate songkick url
        url = self._connection._build_sk_url(self._get_api_path(),
                                             self._query)

        # request event data
        sk_data = self._connection._make_request(url)

        # parse response
        return self._parse_response(sk_data)
