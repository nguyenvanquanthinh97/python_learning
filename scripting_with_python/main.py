from PIL import Image, ImageFilter
from pathlib import Path

image = Image.open(Path("Pokedex", "pikachu.jpg"))
astro_img = Image.open("astro.jpg")

filtered_img = image.filter(ImageFilter.SHARPEN)
grayed_img = image.convert("L")
crooked_img = image.rotate(90)
resized_img = image.resize((300, 300))
crop_size = (100, 100, 400, 400)
region = image.crop(crop_size)
astro_img.thumbnail((200, 200)) # it will resize max is 200 and keep original ratio

filtered_img.save("sharpened_pikachu.png", "png")
grayed_img.save("grayed_pikachu.png", "png")
crooked_img.save("crooked_pikachu.png", "png")
resized_img.save("resized_image.png", "png")
region.save("region.png", "png")
astro_img.save("thumbnail.png", "png")
