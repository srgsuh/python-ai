import cv2
import numpy as np
import create_folders_structure as cfs

WIDTH: int = 256
HEIGHT: int = 256
COLORS = 256
COLOR_GREEN = (0, COLORS - 1, 0)

def write_circle_img(path: str, x_center: int, y_center: int, radius: int) -> None:
    img: np.ndarray = np.full((WIDTH, HEIGHT, 3), COLORS - 1, dtype=np.uint8)
    cv2.circle(img, (x_center, y_center), radius, COLOR_GREEN, -1)
    cv2.imwrite(path, img)

def write_circle_label(path: str, x_center: int, y_center: int, radius: int) -> None:
    x, y = x_center / WIDTH, y_center / HEIGHT
    w, h = 2 * radius / WIDTH, 2 * radius / HEIGHT
    with open(path, 'w') as f:
        f.write(f"0 {x:.6f} {y:.6f}, {w:.6f} {h:.6f}")


if __name__ == '__main__':
    write_circle_img(cfs.IMAGES_TRAIN + cfs.sep + "img01.jpg", 100, 100, 25)
    write_circle_img(cfs.IMAGES_TRAIN + cfs.sep + "img02.jpg", 80, 120, 20)
    write_circle_img(cfs.IMAGES_TRAIN + cfs.sep + "img03.jpg", 120, 130, 100)
    write_circle_img(cfs.IMAGES_TRAIN + cfs.sep + "img04.jpg", 200, 70, 50)

    write_circle_label(cfs.LABELS_TRAIN + cfs.sep + "img01.txt", 100, 100, 25)
    write_circle_label(cfs.LABELS_TRAIN + cfs.sep + "img02.txt", 80, 120, 20)
    write_circle_label(cfs.LABELS_TRAIN + cfs.sep + "img03.txt", 120, 130, 100)
    write_circle_label(cfs.LABELS_TRAIN + cfs.sep + "img04.txt", 200, 70, 50)

    write_circle_img(cfs.IMAGES_VAL + cfs.sep + "img.jpg", 90, 90, 70)

    write_circle_label(cfs.LABELS_VAL + cfs.sep + "img.txt", 90, 90, 70)
    