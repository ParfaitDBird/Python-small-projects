# Decorator
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2-t1} ms')
        return result
    return wrapper


@performance
def long_time():
    print('1')
    for i in range(100000000):
        i*5


@performance
def long_time2():
    print('2')
    for i in list(range(100000000)):
        i*5


long_time()
long_time2()
