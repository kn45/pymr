import sys
import pymr


class MyReducer(pymr.Reducer):
    def __init__(self):
        self.all_cnt = 0
        self.uin = {}

    def flush(self, key, key_cnt):
        print key
        print key_cnt

    def _reduce(self, key, kvalues):
        # @override
        key_cnt = 0
        for kv in kvalues:
            n, value = kv.split('\t')
            key_cnt += 1
            self.all_cnt += 1
        self.flush(key, key_cnt)

    def _cleanup(self):
        # @override
        print self.all_cnt

MyReducer().run()
