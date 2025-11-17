import os

def make_dir(dir_path: str) -> None:
    os.makedirs(dir_path, exist_ok=True)

def join_path(parent_dir_path: str, inner_obj_name: str) -> str:
    return parent_dir_path + os.sep + inner_obj_name

ROOT_DIR = 'datasets'
TRAIN_DIR = join_path(ROOT_DIR, 'train')
TRAIN_IMAGES = join_path(TRAIN_DIR, 'images')
TRAIN_LABELS = join_path(TRAIN_DIR , 'labels')

VAL_DIR = join_path(ROOT_DIR, 'val')
VAL_IMAGES = join_path(VAL_DIR, 'images')
VAL_LABELS = join_path(VAL_DIR , 'labels')

for folder in [TRAIN_IMAGES, TRAIN_LABELS, VAL_IMAGES, VAL_LABELS]:
    make_dir(folder)