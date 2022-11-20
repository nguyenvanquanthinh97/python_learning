from pathlib import Path

# mode = "r+": read and overwrite
# mode = "w": open a file as a new file and write
# mode = "a": append to the EOF.
try :
    with open(Path('assets', 'sad.txt'), mode="r") as my_file:
        text = my_file.read()
        print(text)
except FileNotFoundError as error:
    print('file does not exist')
    raise error

except IOError as error:
    print('error at IO')
    raise error


# my_file = open("test.txt")
# print(my_file.readlines())
# my_file.close()
