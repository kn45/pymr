#!/usr/bin/env python

import sys
from pymr import Mapper, Reducer


class MyMapper(Mapper):
    pass


class MyReducer(Reducer):
    def __init__(self):
        Reducer.__init__(self)
        self.key_fields = 2
        self.all_cnt = 0
        self.uin = {}

    def flush(self, key, key_cnt):
        print key
        print key_cnt

    def _reduce(self, key, values):
        # @override
        key_cnt = 0
        for value in values:
            key_cnt += 1
            self.all_cnt += 1
        self.flush(key, key_cnt)

    def _cleanup(self):
        # @override
        print self.all_cnt


if __name__ == '__main__':
    if sys.argv[1] == 'm':
        MyMapper().run()
    if sys.argv[1] == 'r':
        MyReducer().run()
