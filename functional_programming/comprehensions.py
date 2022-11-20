# comprehended_list = [x * 2 for x in range(3)]
# equate to:
# comprehended_list = []
# for x in range(3):
#   comprehended_list.append(x * 2)

# ---------------------------------------


# comprehended_list = [x * 2 for x in range(3) if x > 1]
# equate to:
# comprehended_list = []
# for x in range(3):
#   if x > 1:
#       comprehended_list.append(x * 2)


# list, set, dictionary
# list
my_list = [char for char in "hello"]
my_list2 = [num for num in range(0, 100)]
my_list3 = [num ** 2 for num in range(0, 100)]
my_list4 = [num * 2 for num in range(0, 5) if num > 3]
print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

# set
my_set = {char for char in "hello"}
my_set2 = {num for num in range(0, 100)}
my_set3 = {num ** 2 for num in range(0, 100)}
my_set4 = {num * 2 for num in range(0, 5) if num > 3}
print(my_set)
print(my_set2)
print(my_set3)
print(my_set4)

# dict
simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value * 2 for key, value in simple_dict.items()}
print(my_dict)

print({num: num * 2 for num in range(4)})
