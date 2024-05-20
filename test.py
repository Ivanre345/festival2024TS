from PIL import Image
import numpy as np


def create_collage(images, collage_size):
    collage = Image.new('RGB', collage_size)

    image_width, image_height = collage_size[0] // len(images), collage_size[1]

    x_offset = 0
    for img_path in images:
        img = Image.open(img_path)
        img = img.resize((image_width, image_height))

        collage.paste(img, (x_offset, 0))
        x_offset += image_width

    return collage


# Пример использования
images_list = ['back_ground1.png', 'button_STICKMAN.png',"D:/project_forTS/stickman/background.gif", "D:/project_forTS/stickman/background 2.gif"]
collage_size = (800, 400)

collage = create_collage(images_list, collage_size)
collage.show()