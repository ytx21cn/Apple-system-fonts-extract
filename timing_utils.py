from time import time
from sys import stderr


def time_func(func, *args, header: str = None,
              start_msg: str = None, end_msg: str = None,
              **kwargs):

    func_name = func.__name__
    header = header or func_name

    print('\n[%s]' % header, file=stderr)
    print('%s' % (start_msg or ('Starting "%s"...' % func_name)),
          file=stderr)

    start_time = time()
    result = func(*args, **kwargs)
    time_elapsed = time() - start_time

    print('\n[%s]' % header, file=stderr)
    print('%s' % (end_msg or ('"%s" completed' % func_name)),
          file=stderr)
    print('Time elapsed: %.3f seconds' % time_elapsed, file=stderr)

    return result
