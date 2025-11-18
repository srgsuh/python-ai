import cv2
import numpy as np
from shape_image import ShapeImage, Color, DEFAULT_COLOR, colors
from random import randint, choice
import math

DEFAULT_COLOR = DEFAULT_COLOR = (0, 0, 255)

class RectangleImage(ShapeImage):
    def __init__(self, x: int, y: int,
                 h_side: int, w_side: int, alpha: float, color: Color = DEFAULT_COLOR):
        """
        Initialize a rotated rectangle.

        Parameters
        ----------
        w, h : int - Image width and height
        x, y : int - Coordinates of the bottom-left vertex of the rectangle.
        h_side : int - rectangle's height.
        w_side : int - rectangle's width.
        alpha : float - Rotation angle in radians between the bottom side and the x-axis.
        Expected to be in the range [0, pi/2). For alpha = 0 the rectangle is axis-aligned.
        For alpha > 0 the rectangle is rotated counterclockwise around its bottom-left vertex.
        color : tuple[int, int, int] - color in BGR format.
        """
        self.color = color

        sin_a, cos_a = math.sin(alpha), math.cos(alpha)
        #rotate initial axis-aligned rectangle and parallel transfer to x and y
        def rotate_and_transfer(x0: float, y0: float) -> tuple[float, float]:
            xr =  x0 * cos_a + y0 * sin_a
            yr = -x0 * sin_a + y0 * cos_a
            return x + xr, y + yr
        #p1,p2,p3,p4 - rectangle vertices after its rotation alpha radians counterclockwise
        self.p1 = x, y
        self.p2 = rotate_and_transfer(0, -h_side)
        self.p3 = rotate_and_transfer(w_side, -h_side)
        self.p4 = rotate_and_transfer(w_side, 0)

    def xywh(self) -> tuple[float, float, float, float]:
        x1, y1 = self.p1
        x2, y2 = self.p2
        x3, y3 = self.p3
        x4, y4 = self.p4

        xx = [x1, x2, x3, x4]
        yy = [y1, y2, y3, y4]

        xmin, xmax = min(xx), max(xx)
        ymin, ymax = min(yy), max(yy)

        x_center = (xmin + xmax) / 2
        y_center = (ymin + ymax) / 2
        width = xmax - xmin
        height = ymax - ymin

        return x_center, y_center, width, height

    def draw(self, canvas: cv2.typing.MatLike) -> None:
        points = np.array(self.points(), dtype=np.int32)
        cv2.fillPoly(canvas, [points], self.color)

    def points(self) -> list[tuple[float, float]]:
        """Return all rectangle points in the clockwise order starting from the upper h_side corner"""
        return [self.p1, self.p2, self.p3, self.p4]

angles: list[float] = [math.radians(x) for x in range(0, 90, 15)]

def random_rectangle(w: int, h: int, min_side = 15) -> ShapeImage:
    max_w = math.floor(w / 3)
    max_h = math.floor(h / math.sqrt(2))
    max_side = min(max_h, max_w)
    if min_side > max_side:
        raise ValueError("The image is too small to contain a rectangle of the given minimum side.")
    x = randint(max_side, w - max_side)
    y = randint(max_side, math.floor(max_side * math.sqrt(2)))
    h_side = randint(min_side, max_side)
    w_side = randint(min_side, max_side)
    alpha = choice(angles)

    return RectangleImage(x, y, h_side, w_side, alpha, choice(colors))
    