import cv2
import numpy as np
from dataclasses import dataclass
from shape_image import ShapeImage

DESC_PATTERN: str = 'circle_x_{x}_y_{y}_r_{r}'

COLOR_GREEN = (0, 255, 0)

@dataclass(frozen=True)
class CircleImage(ShapeImage):
    center: tuple[int, int]
    radius: int
    w: int
    h: int

    def image(self) -> np.ndarray:
        img: np.ndarray = np.zeros((self.w, self.h, 3), dtype=np.uint8)
        cv2.circle(img, self.center, self.radius, COLOR_GREEN, -1)
        return img
    
    def label(self, obj_index: int = 0) -> str:
        x, y = self.center
        x, y = x / self.w, y / self.h
        w, h = 2 * self.radius / self.w, 2 * self.radius / self.h
        return f"{obj_index} {x:.6f} {y:.6f} {w:.6f} {h:.6f}"
    
    def describe(self) -> str:
        x, y = self.center
        return DESC_PATTERN.format(x=x,y=y,r=self.radius)

rng = np.random.default_rng()
def i_rand(min: int, max: int) -> int:
    return int(rng.integers(min, max + 1, dtype=np.uint32))

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
    return CircleImage(center, radius, w, h)

        