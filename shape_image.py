import cv2
import numpy as np
from abc import ABC, abstractmethod

Color = tuple[int,int,int]

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DEFAULT_COLOR = GREEN

colors: list[Color] = [RED, GREEN, BLUE]

class ShapeImage(ABC):
    def label(self, width: int, height: int, obj_index: int = 0) -> str:
        x, y, w, h = self.xywh()
        return f"{obj_index} {x/width:.6f} {y/height:.6f} {w/width:.6f} {h/height:.6f}"
    
    def image(self, width: int, height: int) -> np.ndarray:
        img = np.full((width, height, 3), 0, dtype=np.uint8 )
        self.draw(img)
        return img

    @abstractmethod
    def xywh(self) -> tuple[float, float, float, float]:
        """
        Return a tuple of four floats x, y, w, h, where:
            x, y - coordinates of the center of the shape's box
            w, h - width and height of the shape's box
        """
        pass

    @abstractmethod
    def draw(self, canvas: cv2.typing.MatLike) -> None:
        """Draw the shape on a canvas"""
        pass
        

