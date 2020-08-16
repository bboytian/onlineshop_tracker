# imports
import datetime as dt
from functools import wraps
import os
import sys
import time

from ._modifications import *


# defining decorators
def verbose(func):              # should be placed last
    '''
    Sets verbose mode on function
    while the function is running, stderr is set to __stderr__, i.e. it prints to
    terminal
    '''
    @wraps(func)
    def wrapper_func(*args, verbboo=True, **kwargs):
        if verbboo:
            return func(*args, **kwargs)
        else:
            # closing up previous log files
            prevstdout = None
            prevstderr = None
            if sys.stdout.name != '<stdout>':
                prevstdout = sys.stdout.name
                sys.stdout.close()
            if sys.stderr.name != '<stderr>':
                prevstderr = sys.stderr.name
                sys.stderr.close()
                sys.stderr = sys.__stderr__
            # disabling print
            sys.stdout = open(os.devnull, 'w')
            # running func
            ret = func(*args, **kwargs)
            # enabling print again
            if prevstdout:
                sys.stdout = open(prevstdout, 'a+')
            else:
                sys.stdout = sys.__stdout__
            if prevstderr:
                sys.stderr = open(prevstderr, 'a+')
            return ret
    return wrapper_func


def timer(_func=None, *, ntimes=1000):
    """Print the runtime of the decorated function"""
    def decorator_func(func):
        @wraps(func)
        def wrapper_func(*args, **kwargs):
            starttime = time.time()
            for i in range(ntimes):
                wrapperret= func(*args, **kwargs)
            print("finished {} {}times in {:.4f}s".format(
                func.__name__, ntimes,
                time.time() - starttime
            ))
            return wrapperret
        return wrapper_func
    if _func:
        return decorator_func(_func)
    else:
        return decorator_func


def announcer(_func=None, *, endboo=True, newlineboo=False):
    '''anounces when function is called and when it finishes; if specified'''
    def decorator_func(func):
        @wraps(func)
        def wrapper_func(*args, **kwargs):
            startstr = '{:%Y%m%d%H%M} run {}.{}...'.format(
                dt.datetime.now(),
                func.__module__, func.__name__
            )
            if newlineboo and not endboo:
                startstr += '\n'
            print(startstr)
            wrapperret = func(*args, **kwargs)

            endstr = '{:%Y%m%d%H%M} end {}.{}'.format(
                dt.datetime.now(),
                func.__module__, func.__name__
            )

            if endboo:
                if newlineboo:
                    endstr += '\n'
                print(endstr)
            return wrapperret
        return wrapper_func
    if _func:
        return decorator_func(_func)
    else:
        return decorator_func
