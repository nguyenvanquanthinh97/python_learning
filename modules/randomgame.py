from random import randrange
from sys import argv


def random_game(start, end):
    start = int(start)
    end = int(end)
    answer = randrange(start, end)
    print(f'answer: {answer}')
    while True:
        try:
            guess = int(input("Input your guess: "))

            if guess == answer:
                print('Congratulation! you guess correct')
                break

            if not start < guess < end:
                print(f'correct answer is in from {start} to {end - 1}')

            print("Wrong !!! guess again")
        except ValueError:
            print("Please input a number")

        continue


if __name__ == "__main__":
    start = argv[1]
    end = argv[2]
    random_game(start, end)
