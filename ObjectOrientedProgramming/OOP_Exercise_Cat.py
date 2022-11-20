# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Cat 01', 1)
cat2 = Cat('Cat 02', 2)
cat3 = Cat('Cat 03', 3)


# 2 Create a function that finds the oldest cat
def get_oldest_cat(*args):
    oldest_cat = args[0]
    for cat in args:
        if oldest_cat.age < cat.age:
            oldest_cat = cat
    return oldest_cat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest_cat = get_oldest_cat(cat1, cat2, cat3)
print(f'The oldest cat is {oldest_cat.age} years old.')
