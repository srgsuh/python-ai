import os
from os.path import join

def clear_all_files(root: str):
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            os.remove(join(dirpath, filename))

ROOT_DIR = 'datasets'

IMAGE_SUB = 'images'
LABEL_SUB = 'labels'

TRAIN_DIR = join(ROOT_DIR, 'train')
TRAIN_IMAGES = join(TRAIN_DIR, IMAGE_SUB)
TRAIN_LABELS = join(TRAIN_DIR , LABEL_SUB)

VAL_DIR = join(ROOT_DIR, 'val')
VAL_IMAGES = join(VAL_DIR, IMAGE_SUB)
VAL_LABELS = join(VAL_DIR , LABEL_SUB)

for folder in [TRAIN_IMAGES, TRAIN_LABELS, VAL_IMAGES, VAL_LABELS]:
    os.makedirs(folder, exist_ok=True)