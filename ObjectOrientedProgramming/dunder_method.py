# By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class.
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        print("deleted")
        return "deleted"

    def __call__(self):
        return ('yes??')

    def __getitem__(self, i):
        return self.my_dict[i]

    def __repr__(self):
        return "Toy object"

    def __format__(self, format_spec):
        return format(8/100, '%')

    # Gets called when the item is not found via __getattribute__
    def __getattr__(self, item):
        print('__getattr__')
        return self.my_dict[item]

    # Gets called when an attribute is accessed
    def __getattribute__(self, item):
        print('__getattribute__')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print(f'__setattr__ {key} - {value}')
        return object.__setattr__(self, key, value)


action_figure = Toy('red', 0)  # __init__(self)
print(action_figure.__str__())  # we can invoke the dunder method directly but should not do that
print(str(action_figure))  # __str__(self)
print(len(action_figure))  # __len__(self)
print(action_figure())  # __call__(self)
print(action_figure['name'])  # __getitem__(self,i)
print(repr(action_figure))
print(format(action_figure))
print(action_figure.name)

action_figure.woohoo = True
print(action_figure.woohoo)

del action_figure

