import cv2
import numpy as np
from os.path import join
from create_folders import TRAIN_DIR,VAL_DIR,IMAGE_SUB,LABEL_SUB, clear_all_files
from circle_image import random_circle
from shape_image import ShapeImage

WIDTH: int = 256
HEIGHT: int = 256
IMAGE_EXT = '.jpg'
LABEL_EXT = '.txt'
N_TESTS = 8

def save_text(file_path: str, text: str) -> None:
    with open(file_path, 'w') as f:
        f.write(text)

def save_image(file_path: str, img: np.ndarray) -> None:
    cv2.imwrite(file_path, img)

def save_training_case(parent_folder: str, f_name: str, shape: ShapeImage) -> None:
    save_text(join(parent_folder, LABEL_SUB, f_name+LABEL_EXT), shape.label())
    save_image(join(parent_folder, IMAGE_SUB, f_name+IMAGE_EXT), shape.image())


def generate_test_circles(parent_folder: str, n_tests: int) -> None:
    for idx in range(1, n_tests + 1):
        shape: ShapeImage = random_circle(WIDTH, HEIGHT)
        save_training_case(parent_folder, 'circle_'+str(idx).zfill(3), shape)

if __name__ == '__main__':
    clear_all_files(TRAIN_DIR)
    clear_all_files(VAL_DIR)
    generate_test_circles(TRAIN_DIR, N_TESTS)
    generate_test_circles(VAL_DIR, max(1, N_TESTS // 10))
        