import cv2
import numpy as np
from shape_image import ShapeImage, i_rand, COLOR_GREEN

DESC_PATTERN: str = 'circle_x{x}_y{y}_r{r}'

class CircleImage(ShapeImage):
    def __init__(self, w: int, h: int,  center: tuple[int, int], radius: int):
        super().__init__(w, h)
        self.center = center
        self.radius = radius

    def xywh(self) -> tuple[float, float, float, float]:
        x, y = self.center
        x, y = x / self.w, y / self.h
        w, h = 2 * self.radius / self.w, 2 * self.radius / self.h
        return x, y, w, h

    def image(self) -> np.ndarray:
        img: np.ndarray = super().empty_image()
        cv2.circle(img, self.center, self.radius, COLOR_GREEN, -1)
        return img
    
    def describe(self) -> str:
        x, y = self.center
        return DESC_PATTERN.format(x=x,y=y,r=self.radius)


def random_circle(img_width: int, img_height: int | None = None) -> ShapeImage:
    w, h = img_width, img_width if img_height is None else img_height
    if w < 3 or h < 3:
        raise ValueError("Image is too small to fit a circle")
    min_size: int = min(w, h)
    radius: int = i_rand(1, (min_size - 1) // 2)
    diameter: int = 2 * radius + 1
    left_x: int = i_rand(0, w - diameter)
    upper_y: int = i_rand(0, h - diameter)

    center = (left_x + radius, upper_y + radius)
    return CircleImage(w, h, center, radius)

        