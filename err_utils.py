def get_err_msg(err: BaseException, break_line: bool = False) -> str:
    """
    Get the error message string for specified error
    :param err: the exception object
    :param break_line: whether to put exception name and message on two lines
    :return: the error message string
    """
    return '\n[%s]%s%s' % (type(err).__name__,
                           '\n' if break_line else ' ', err)
