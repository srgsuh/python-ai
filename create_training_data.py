import cv2
import numpy as np
from create_folders import TRAIN_DIR,VAL_DIR,IMAGE_SUB,LABEL_SUB,join_path
from circle_image import random_circle, CircleImage
from shape_image import ShapeImage
import math
import os

WIDTH: int = 256
HEIGHT: int = 256
IMAGE_EXT = '.jpg'
LABEL_EXT = '.txt'
N_TESTS = 100

def clear_all_files(root: str):
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            os.remove(os.path.join(dirpath, filename))

def build_path(parent: str, sub: str, name: str, ext: str) -> str:
    folder: str = join_path(parent, sub)
    return join_path(folder, name + ext)

def write_test_case(parent_folder: str, f_name: str, shape: ShapeImage) -> None:
    label_path = build_path(parent_folder, LABEL_SUB, f_name, LABEL_EXT)
    with open(label_path, 'w') as f:
        f.write(shape.label())
    image_path = build_path(parent_folder, IMAGE_SUB, f_name, IMAGE_EXT)
    cv2.imwrite(image_path, shape.image())

def generate_test_circles(parent_folder: str, n_tests: int) -> None:
    prefix_length: int = 1 + math.ceil(math.log10(n_tests))
    for idx in range(1, n_tests + 1):
        s_idx = str(idx).zfill(prefix_length)
        shape: ShapeImage = random_circle(WIDTH, HEIGHT)
        write_test_case(parent_folder, s_idx + shape.describe(), shape)

if __name__ == '__main__':
    clear_all_files(TRAIN_DIR)
    clear_all_files(VAL_DIR)
    generate_test_circles(TRAIN_DIR, N_TESTS)
    generate_test_circles(VAL_DIR, N_TESTS // 10)
        