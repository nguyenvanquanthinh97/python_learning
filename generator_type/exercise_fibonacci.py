def fib(number):
    prev_result = result = 0
    for i in range(number):
        if i == 1:
            result = 1
        else:
            prev_prev_result = prev_result
            prev_result = result
            result = prev_prev_result + prev_result
        yield result


for i, x in enumerate(fib(20)):
    print(f'fib[{i}] = {x}')
