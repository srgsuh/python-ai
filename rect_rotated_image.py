import cv2
import numpy as np
from shape_image import ShapeImage
from random import randint, choice
import math

class RectRotatedImage(ShapeImage):
    def __init__(self, w: int, h: int, x: int, y: int, left: int, right: int, alpha: float):
        super().__init__(w, h)
        sin_a, cos_a = math.sin(alpha), math.cos(alpha)
        self.p1 = x, y
        self.p2 = x - left * sin_a, y - left * cos_a
        self.p4 = x + right * cos_a, y - right * sin_a
        x4, y4 = self.p4
        self.p3 = x4 - left * sin_a, y4 - left * cos_a
        self.center = [x + left * sin_a, y - left * cos_a]

    def xywh(self) -> tuple[float, float, float, float]:
        _, y1 = self.p1
        x2, _ = self.p2
        _, y3 = self.p3
        x4, _ = self.p4

        x = (x2 + x4) / 2
        y = (y3 + y1) / 2
        w = (x4 - x2)
        h = (y1 - y3)
        return x/self.w, y/self.h, w/self.w, h/self.h

    def draw(self, canvas: cv2.typing.MatLike) -> None:
        points = np.array(self.points(), dtype=np.int32)
        cv2.fillPoly(canvas, [points], (0, 255, 0))

    def points(self) -> list[tuple[float, float]]:
        """Return all rectangle points in the clockwise order starting from the upper left corner"""
        return [self.p1, self.p2, self.p3, self.p4]

angles: list[float] = [math.radians(x) for x in range(0, 90, 10)]

def random_rotated_rect(w: int, h: int, min_side = 10, max_side = 80) -> ShapeImage:
    x = randint(max_side, w - max_side)
    y = randint(max_side, h - max_side)
    left = randint(min_side, max_side)
    right = randint(min_side, max_side)
    alpha = choice(angles)

    return RectRotatedImage(w, h, x, y, left, right, alpha)
    