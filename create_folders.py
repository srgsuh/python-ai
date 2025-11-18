import os

def join_path(parent_dir_path: str, inner_obj_name: str) -> str:
    return parent_dir_path + os.sep + inner_obj_name

ROOT_DIR = 'datasets'

IMAGE_SUB = 'images'
LABEL_SUB = 'labels'

TRAIN_DIR = join_path(ROOT_DIR, 'train')
TRAIN_IMAGES = join_path(TRAIN_DIR, IMAGE_SUB)
TRAIN_LABELS = join_path(TRAIN_DIR , LABEL_SUB)

VAL_DIR = join_path(ROOT_DIR, 'val')
VAL_IMAGES = join_path(VAL_DIR, IMAGE_SUB)
VAL_LABELS = join_path(VAL_DIR , LABEL_SUB)

for folder in [TRAIN_IMAGES, TRAIN_LABELS, VAL_IMAGES, VAL_LABELS]:
    os.makedirs(folder, exist_ok=True)