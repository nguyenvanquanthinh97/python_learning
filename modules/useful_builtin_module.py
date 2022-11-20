from collections import Counter, defaultdict, OrderedDict
from array import array
import datetime

counter = Counter([1, 2, 3, 4, 5, 6, 6])
print(counter)

d = defaultdict(lambda: 0, {'a': 2, 'b': 3})
print(d['c'])
print(d['a'])

# Recently, the Python has made Dictionaries ordered by default!
# So unless you need to maintain older version of Python (older than 3.7)
# you no longer need to use ordered dict, you can just use regular dictionaries!
# https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/
order_dict1 = OrderedDict()
order_dict1['a'] = 1
order_dict1['b'] = 2

order_dict2 = OrderedDict()
order_dict2['b'] = 2
order_dict2['a'] = 1

print(order_dict1 == order_dict2)
print({'a': 1, 'b': 2} == {'b': 2, 'a': 1})

print(datetime.date.today())
print(datetime.time(22, 30, 30))

arr = array('i', [1, 2, 3])
print(arr)
print(arr[1])
arr.append(4)
print(arr)
