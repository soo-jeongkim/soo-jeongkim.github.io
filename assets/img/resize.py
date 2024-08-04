import os
import PIL
from PIL import Image

def resize_image(fpath: str) -> PIL.Image.Image:
    img = Image.open(fpath)
    resized_image = img.resize((659, 1000))
    return resized_image

dirname = "/Users/soojeong/Documents/soo-jeongkim.github.io/assets/img/bookcover"
fnames = os.listdir(dirname)

if __name__ == "__main__":
    for fname in fnames:
        fpath = os.path.join(dirname, fname)
        resized_image = resize_image(fpath)
        resized_image.save(fpath)
