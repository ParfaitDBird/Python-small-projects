# DECORATORS
def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func


'''
by adding the sintax @my_decorator
I can add extra functionality to other functions
'''


def hello():
    print('Hello')


@my_decorator
def bye():
    print('see ya!')


my_decorator(hello)()
# hello()
bye()
