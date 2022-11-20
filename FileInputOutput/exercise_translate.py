from pathlib import Path
from translate import Translator

try:
    with open(Path('assets', 'sad.txt')) as my_file:
        content = my_file.read()
except FileNotFoundError as err:
    print("File not found:", err)
except IOError as err:
    print("IO error:", err)

translator = Translator(to_lang="ja")
translation = translator.translate(content)
print(translation)


try:
    with open(Path("assets", "sad-ja.txt"), mode="w") as my_file:
        my_file.write(translation)
except IOError as err:
    print("IO error:", err)


