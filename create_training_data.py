from os.path import join
from create_folders import TRAIN_DIR,VAL_DIR,IMAGE_SUB,LABEL_SUB
from circle_image import random_circle, CircleImage
from rectangle_image import RectangleImage, random_rectangle
from shape_image import ShapeImage
from utils import write_image, write_text, empty_folders
import numpy as np


WIDTH: int = 256
HEIGHT: int = 256
IMAGE_EXT = '.jpg'
LABEL_EXT = '.txt'
N_TESTS = 30

def write_training_case(parent_folder: str, f_name: str, shape: ShapeImage, obj_index: int = 0) -> None:
    label_name = join(parent_folder, LABEL_SUB, f_name+LABEL_EXT)
    image_name = join(parent_folder, IMAGE_SUB, f_name+IMAGE_EXT)
    write_text(label_name, shape.label(WIDTH, HEIGHT, obj_index))
    write_image(image_name, shape.image(WIDTH, HEIGHT))

def generate_training_cases(parent_folder: str, n_tests: int) -> None:
    for idx in range(1, n_tests + 1):
        circle: ShapeImage = random_circle(WIDTH, HEIGHT, 8)
        rect: ShapeImage = random_rectangle(WIDTH, HEIGHT)
        write_training_case(parent_folder, 'circle_'+str(idx).zfill(3), circle, 0)
        write_training_case(parent_folder, 'rectangle_'+str(idx).zfill(3), rect, 1)

if __name__ == '__main__':
    empty_folders(TRAIN_DIR, VAL_DIR)
    generate_training_cases(TRAIN_DIR, N_TESTS)
    generate_training_cases(VAL_DIR, max(1, N_TESTS // 10))