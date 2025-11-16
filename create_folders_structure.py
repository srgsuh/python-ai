import os

ROOT_DIR = 'datasets'
IMAGES = ROOT_DIR + os.sep + 'images'
IMAGES_TRAIN = IMAGES + os.sep + 'train'
IMAGES_VAL = IMAGES + os.sep + 'val'
LABELS = ROOT_DIR + os.sep + 'labels'
LABELS_TRAIN = LABELS + os.sep + 'train'
LABELS_VAL = LABELS + os.sep + 'val'

os.makedirs(IMAGES_TRAIN, exist_ok=True)
os.makedirs(IMAGES_VAL, exist_ok=True)

os.makedirs(LABELS_TRAIN, exist_ok=True)
os.makedirs(LABELS_VAL, exist_ok=True)