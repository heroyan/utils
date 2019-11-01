# -*- coding: utf-8 -*-
'''
'''
import random
import threading

class SequenceGenerator(object):
    '''序号生成器
    '''
    def __init__(self, min_val = 0, max_val = 0xffffffff):
        self._min = min_val
        self._max = max_val
        self._curr = random.randint(min_val, max_val)
        self._lock = threading.Lock()
    
    def next(self):
        with self._lock:
            self._curr += 1
            if self._curr > self._max:
                self._curr = self._min
            return self._curr

if __name__ == '__main__':
    s = SequenceGenerator()
    print s.next()
    print s.next()
    print s.next()