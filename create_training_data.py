from os.path import join
from create_folders import TRAIN_DIR,VAL_DIR,IMAGE_SUB,LABEL_SUB
from circle_image import random_circle
from shape_image import ShapeImage
from utils import write_image, write_text, empty_folders

WIDTH: int = 256
HEIGHT: int = 256
IMAGE_EXT = '.jpg'
LABEL_EXT = '.txt'
N_TESTS = 20

def create_training_case(parent_folder: str, f_name: str, shape: ShapeImage, obj_index: int = 0) -> None:
    write_text(join(parent_folder, LABEL_SUB, f_name+LABEL_EXT), shape.label(obj_index))
    write_image(join(parent_folder, IMAGE_SUB, f_name+IMAGE_EXT), shape.image())


def generate_test_circles(parent_folder: str, n_tests: int) -> None:
    for idx in range(1, n_tests + 1):
        shape: ShapeImage = random_circle(WIDTH, HEIGHT)
        create_training_case(parent_folder, 'circle_'+str(idx).zfill(3), shape, 0)

if __name__ == '__main__':
    empty_folders(TRAIN_DIR, VAL_DIR)
    generate_test_circles(TRAIN_DIR, N_TESTS)
    generate_test_circles(VAL_DIR, max(1, N_TESTS // 10))
        