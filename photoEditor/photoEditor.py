from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'C:\\Users\\joudj\\CODE.JJ\\photoEditor\\imgs'
pathOut = 'C:\\Users\joudj\\CODE.JJ\\photoEditor\\editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit= img.filter(ImageFilter.SHARPEN).convert('L')
   

      
    clean_name = os.path.splitext(filename)[0]

    edit.save(f"{pathOut}/{clean_name}_edited.jpg")
    