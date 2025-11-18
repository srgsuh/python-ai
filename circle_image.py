import cv2
import numpy as np
from shape_image import ShapeImage
from random import randint

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
        img: np.ndarray = np.zeros((self.w, self.h, 3), dtype=np.uint8)
        cv2.circle(img, self.center, self.radius, (0, 255, 0), -1)
        return img
    
    def describe(self) -> str:
        x, y = self.center
        return DESC_PATTERN.format(x=x,y=y,r=self.radius)


def random_circle(w: int, h: int, min_radius: int = 5) -> ShapeImage:
    """
    Generate an image of size (w × h) containing a randomly positioned circle.
    The circle’s radius is chosen randomly but is at least `min_radius` pixels.
    """
    min_diameter = 2 * min_radius + 1
    if w < min_diameter or h < min_diameter:
        raise ValueError("The image is too small to contain a circle of the given minimum radius.")

    radius: int = randint(min_radius, (min(w, h) - 1) // 2)
    diameter: int = 2 * radius + 1
    left_x: int = randint(0, w - diameter)
    upper_y: int = randint(0, h - diameter)

    center = (left_x + radius, upper_y + radius)
    return CircleImage(w, h, center, radius)

        