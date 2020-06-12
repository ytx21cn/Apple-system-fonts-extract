from time import time
from sys import stderr


def time_func(func):
    """
    NOTE: This is a decorator function.

    Execute a function :param func with arguments,
    and print the time it has taken.

    :param func: the function to execute.
    :return: the inner function.
    """

    func_name = func.__name__

    def inner_func(*args, **kwargs):

        print('\n[Starting "%s"...]' % func_name,
              'Timing starts.',
              sep='\n', file=stderr)

        start_time = time()
        result = func(*args, **kwargs)
        time_elapsed = time() - start_time

        print('\n["%s" completed]' % func_name,
              'Time elapsed: %.3f seconds.' % time_elapsed,
              sep='\n', file=stderr)
        return result

    return inner_func
