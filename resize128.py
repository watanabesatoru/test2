import os
import glob

from PIL import Image
#
def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result



files = glob.glob('./image/*.jpg')



for f in files:


    im = Image.open(f)

    im_new = expand2square(im, (255, 255, 255))

    im_new = im_new.resize((128, 128),Image.LANCZOS)

    f = f.replace('image' , 'image128')

    print(f) # https://teratail.com/questions/57459

    im_new.save(f)
