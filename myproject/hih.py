def multiply_by_two(num):
    return num * 2


def parent():
    total = 0

    def counting():
        nonlocal total
        total += 1

    counting()
    counting()
    return total


print(parent())
print(multiply_by_two(3))
