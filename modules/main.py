# careful name collision
# recommended define import module as it explicitly telling what specific functions we will use
from utility import divide, multiply

from shopping.more_shopping import shopping_cart

# every file running with python3 {file_name}.py has __name__ is "__main__"
if __name__ == '__main__':
    print(multiply(3, 8))
    print(shopping_cart.buy("apple"))
