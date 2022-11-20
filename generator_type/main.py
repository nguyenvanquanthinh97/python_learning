# all generators are iterators
# but not every iterators are generators

def generator_function(num):
    for i in range(num):
        # 'yield' stop the program. Only continue when call 'next'
        yield i * 2


g = generator_function(2)
next(g)
print(next(g))
next(g)
# for i in generator_function(10):
#     print(i)
