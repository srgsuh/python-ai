import cv2
import numpy as np
from shape_image import ShapeImage
from random import randint

DESC_PATTERN: str = 'rect_x{x1}_y{y1}_x{x2}_y{y2}'

class RectangleImage(ShapeImage):
    def __init__(self, w: int, h: int, x1: int, y1: int, x2: int, y2: int):
        super().__init__(w, h)
        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)
        self.xmin, self.ymin = xmin, ymin
        self.xmax, self.ymax = xmax, ymax
    
    def describe(self) -> str:
        return DESC_PATTERN.format(x1=self.xmin,y1=self.ymin,x2=self.xmax,y2=self.ymax)

    def image(self) -> np.ndarray:
        img = np.zeros((self.w, self.h, 3), dtype=np.uint8)
        points = np.array(
            [[self.xmin,self.ymin],[self.xmax,self.ymin],[self.xmax,self.ymax],[self.xmin,self.ymax]]
            ,dtype=np.int32
        )
        cv2.fillPoly(img, [points], (255, 0, 0))
        return img
    
    def xywh(self) -> tuple[float, float, float, float]:
        w: float = self.xmax - self.xmin
        h: float = self.ymax - self.ymin
        x: float = (self.xmin + 0.5*w) / self.w
        y: float = (self.ymin + 0.5*h) / self.h
        return x, y, w / self.w, h / self.h
        
def random_rectangle(w: int, h: int, min_side: int = 5) -> ShapeImage:
    """
    Generate an image of size (w × h) containing a randomly positioned rectangle.
    The rectangle's sides is chosen randomly but each of then at least `min_side` pixels.
    """
    if w < min_side or h < min_side:
        raise ValueError("The image is too small to contain a rectangle of the given minimum side.")
    xmin: int = randint(0, w - min_side)
    ymin: int = randint(0, h - min_side)
    xmax: int = randint(xmin + min_side, w)
    ymax: int = randint(ymin + min_side, h)
    return RectangleImage(w, h, xmin, ymin, xmax, ymax)