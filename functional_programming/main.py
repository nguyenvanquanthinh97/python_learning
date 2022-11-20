from functools import reduce

# map, filter, zip and reduce
my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = [100, 200]

# map
print(list(map(lambda item: item * 2, my_list)))
print(my_list)


# filter
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(my_list)

# zip
print(list(zip(my_list, your_list, their_list)))


# reduce
print(reduce(lambda acc, item: acc + item, my_list, 0))
