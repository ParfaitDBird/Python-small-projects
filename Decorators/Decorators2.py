# DECORATORS
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrap_func


@my_decorator
def hello(greeting, emoji='xd'):
    print(greeting, emoji)


hello('fuck')

# MORE INFO READING ABOUT DECORATOR PATTERN
