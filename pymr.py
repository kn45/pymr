import sys
from operator import itemgetter
from itertools import imap, groupby
from abc import ABCMeta


class Mapper(object):
    """override in subclass:
    _setup
    _map
    _cleanup
    """
    def __init__(self):
        return

    def _setup(self):
        return

    def _map(self, inl):
        print inl

    def _cleanup(self):
        return

    def run(self):
        self._setup()
        for line in sys.stdin:
            self._map(line.rstrip('\r\n'))
        self._cleanup()


class Reducer(object):
    """override in subclass:
    _setup
    _map
    _cleanup
    """
    def __init__(self):
        return

    def _get_key(self, inl):
        # extract the key from one data line
        return inl.rstrip('\r\n').split('\t')[0]

    def run(self):
        self._setup()
        stdin_strip = imap(lambda l: l.rstrip('\r\n'), sys.stdin)
        for key, kvalues in groupby(stdin_strip, self._get_key):
            self._reduce(key, kvalues)
        self._cleanup()

    def _setup(self):
        return

    def _reduce(self, key, kvalues):
        for kv in kvalues:
            print kv

    def _cleanup(self):
        return

if __name__ == '__main__':
    Reducer().run()
