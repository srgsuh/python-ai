import os

sep = os.sep

ROOT_DIR = 'datasets'
IMAGES = ROOT_DIR + sep + 'images'
IMAGES_TRAIN = IMAGES + sep + 'train'
IMAGES_VAL = IMAGES + sep + 'val'
LABELS = ROOT_DIR + sep + 'labels'
LABELS_TRAIN = LABELS + sep + 'train'
LABELS_VAL = LABELS + sep + 'val'

os.makedirs(IMAGES_TRAIN, exist_ok=True)
os.makedirs(IMAGES_VAL, exist_ok=True)

os.makedirs(LABELS_TRAIN, exist_ok=True)
os.makedirs(LABELS_VAL, exist_ok=True)