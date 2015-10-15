from connection import SongkickConnection as Songkick


__author__ = 'Matt Dennewitz and David Renne'
__version__ = '0.1.0'
__version_info__ = tuple(__version__.split('.'))


__all__ = ['Songkick']


def get_version():
    return __version__
