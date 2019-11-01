# -*- coding: utf-8 -*-

import time
import traceback

class RetryLimitError(Exception):
    '''超过重试错误
    '''
    pass
     
class RetryLimit(object):
    '''限定次数的重试操作
    '''
    def __init__(self, max_count, interval):
        self._max = max_count
        self._interval = interval
        
    def retry(self, 
        func, 
        args, 
        exceptions = (Exception), 
        resultmatcher = None):
        '''重试
        '''
        count = 0
        while True:
            try:
                ret = func(*args)
                if resultmatcher is None:
                    return ret
                else:
                    if resultmatcher(ret) == True:
                        return ret
                count += 1
                if count >= self._max:
                    raise RetryLimitError('尝试了%d次，结果为%s'%(count, str(ret)))
                    
            except exceptions:
                count += 1
                if count >= self._max:
                    raise RetryLimitError('尝试了%d次，异常为:\n%s'%(count, traceback.format_exc()))
                
            time.sleep(self._interval)
        return ret


def test(age):
    print 'run in method test', age

    return {'ret': 1}

if __name__ == '__main__':
    RetryLimit(3, 1).retry(test, (1234, ), (Exception, ), lambda x: x['ret'] == 0)