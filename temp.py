from time import time
from time import sleep

def count_time():
    def tmp(func):
        def wrapped(*args, **kargs):
            begin_time = time()
            result = func(*args, **kargs)
            end_time = time()
            cost_time = end_time - begin_time
            print '%s called cost time : %s' %(func.__name__, cost_time)
            return result
        return wrapped
    return tmp
