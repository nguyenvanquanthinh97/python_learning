# under the hood of for...loop
# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator))
#         except StopIteration:
#             break
#
#
# special_for([1, 2, 3])


# under the hood of range(start,end,step) builtin function
# or we can under the hood of generator
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


for i in MyRange(0, 5):
    print(i * 3)
