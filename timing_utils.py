from time import time
from sys import stderr


def time_func(func, *args, header: str = None,
              start_msg: str = None, end_msg: str = None,
              **kwargs):
    """
    Execute a function :param func with arguments
    and print the time it has taken.
    Header can be customized with :param header
    Custom messages can be customized with :param start_msg and :param end_msg
    :param func: the function to execute
    :param args: positional arguments for :param func
    :param header: custom header to print
        before :param start_msg and :param end_msg
    :param start_msg: the message to print before :param func starts
    :param end_msg: the message to print after :param func ends
    :param kwargs: keyword arguments for :param func
    :return: the execution result of :param func
    """

    func_name = func.__name__
    header = header or func_name

    print('\n[%s]' % header, start_msg or ('Starting "%s"...' % func_name),
          sep='\n', file=stderr)

    start_time = time()
    result = func(*args, **kwargs)
    time_elapsed = time() - start_time

    print('\n[%s]' % header, end_msg or ('"%s" completed' % func_name),
          'Time elapsed: %.3f seconds' % time_elapsed,
          sep='\n', file=stderr)

    return result
