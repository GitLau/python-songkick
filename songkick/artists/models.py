from ..base import SongkickModel
from .. import fields
from ..events.models import SongkickEvent


class SongkickArtist(SongkickModel):
    """A Songkick-described artist.

    :param id: Songkick id
    :param songkick_uri: Songkick artist detail uri
    :param display_name: Artist name, eg, "Neil Young".
    :param on_tour_until: On tour end date
    """

    id = fields.Field(mapping='id')
    songkick_uri = fields.Field(mapping='uri')
    display_name = fields.Field(mapping='displayName')
    on_tour_until = fields.Field(mapping='onTourUntil')

    def __repr__(self):
        return self.display_name.encode('utf-8')