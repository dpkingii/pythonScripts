from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'  #folder for unedited images
pathOut = './editedImages' #folder for edited images

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    #shapening
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'./{pathOut}/{clean_name}_edited.jpg')