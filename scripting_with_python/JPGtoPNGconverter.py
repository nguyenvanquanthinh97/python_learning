import sys
import os
from pathlib import Path
from PIL import Image


def convert_jpg_to_png(src, dest):
    # check is new exists, if not create
    is_exist_dest = os.path.exists(dest)
    if not is_exist_dest:
        os.makedirs("new")

    # loop through Pokedex
    filenames = os.listdir(src)
    for filename in filenames:
        src_file = Path(src, filename)
        dest_file = Path(dest, convert_filename_to_png(filename))
        img = Image.open(src_file)
        img.save(dest_file, "png")
        print(f"{dest_file} done!")


def convert_filename_to_png(path):
    name, _ = os.path.splitext(path)
    return name + '.png'


if __name__ == '__main__':
    # grab first asn second argument
    src = sys.argv[1]
    dest = sys.argv[2]
    convert_jpg_to_png(src, dest)
