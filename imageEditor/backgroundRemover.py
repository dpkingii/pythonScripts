from rembg import remove

from PIL import Image
import os

path = './images'  #folder for unedited images
pathOut = './editedImages' #folder for edited images

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = remove(img)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'./{pathOut}/{clean_name}_rembg.png')

