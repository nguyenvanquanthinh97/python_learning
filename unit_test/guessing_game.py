import random


def guessing_game():
    answer = random.randint(1, 10)
    while True:
        guess = input('guess a number 1~10: ')
        result = check_correct_guessing(guess, answer)

        if result:
            print(result)

        if result == 'you are a genius!':
            break


def check_correct_guessing(guess, answer):
    try:
        guess = int(guess)
        if 0 < guess < 11:
            if guess == answer:
                return 'you are a genius!'
        else:
            return 'hey bozo, i said 1~10'
    except ValueError:
        return 'please enter a number'


if __name__ == '__main__':
    guessing_game()
