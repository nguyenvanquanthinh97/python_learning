# Decorator
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('********')

    return wrap_func


# This decorator works like: hello = decorator(hello)
@my_decorator
def hello(greeting, emoji=':))'):
    print(greeting, emoji)


hello("Hello there")

from time import time


def performance(func):
    def wrapper_func(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f'took {end - start} second')

    return wrapper_func


@performance
def long_time_function():
    for i in range(100000000):
        i * 5


long_time_function()
