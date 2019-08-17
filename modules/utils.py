import time
from functools import wraps


def thyme(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = f(*args, **kwargs)
        end = time.perf_counter()
        print('Function {0} took {1} seconds.'.format(f.__name__, round(end-start, 6)))
        return result
    return wrapper
