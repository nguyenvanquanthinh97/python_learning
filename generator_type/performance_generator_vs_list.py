from time import time
# As the result handling long loop or long list data.
# It always efficient when handling generator rather than list
# Due to generator will not initially taking a long list of item, instead it just give the use each item
# when the program calling 'next'. Hence it is much better about memory and time execution

def performance(fn):
    def wrapper(*args, **kwargs):
        start = time()
        fn(*args, **kwargs)
        end = time()
        print(f'Execution time: {end - start} seconds')

    return wrapper


@performance
def long_time_using_generator(num):
    print('generator')
    for i in range(num):
        i * 5


@performance
def long_time_using_list(num):
    print('list')
    for i in list(range(num)):
        i * 5


num = 100000000
long_time_using_generator(num)
long_time_using_list(num)
