# https://github.com/kn45/PyMR
import sys
from abc import ABCMeta
from itertools import imap, groupby
from operator import itemgetter


class Mapper(object):
    """override in subclass:
    _setup(self)
    _map(self, inl)
    _cleanup(self)
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
    _setup(self)
    _reduce(self, key, values)
    _cleanup(self)
    self.delim
    self.key_fields
    """
    def __init__(self):
        self.delim = '\t'
        self.key_fields = 1

    def _get_kv(self, tar):
        def __get_kv(inl):
            """generate key-value pair
            tar=0, return key; tar=1, return value"""
            fields = inl.split(self.delim)
            return (self.delim.join(fields[:self.key_fields]),
                    self.delim.join(fields[self.key_fields:]))[tar]
        return __get_kv

    def run(self):
        self._setup()
        stdin_strip = imap(lambda l: l.rstrip('\r\n'), sys.stdin)
        for key, kvalues in groupby(stdin_strip, self._get_kv(0)):
            values = imap(self._get_kv(1), kvalues)
            self._reduce(key, values)
        self._cleanup()

    def _setup(self):
        return

    def _reduce(self, key, values):
        print key
        for value in values:
            print value

    def _cleanup(self):
        return


if __name__ == '__main__':
    Reducer().run()
