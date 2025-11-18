import cv2
import numpy as np
from abc import ABC, abstractmethod

class ShapeImage(ABC):
    def __init__(self, w: int, h: int):
        self.w, self.h = w, h
    
    def label(self, obj_index: int = 0) -> str:
        x, y, w, h = self.xywh()
        return f"{obj_index} {x:.6f} {y:.6f} {w:.6f} {h:.6f}"
    
    def image(self) -> np.ndarray:
        img = np.zeros((self.w, self.h, 3), dtype=np.uint8)
        self.draw(img)
        return img

    @abstractmethod
    def xywh(self) -> tuple[float, float, float, float]:
        pass

    @abstractmethod
    def draw(self, canvas: cv2.typing.MatLike) -> None:
        pass
        

