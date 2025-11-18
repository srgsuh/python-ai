import numpy as np
from abc import ABC, abstractmethod

COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (255, 0, 0)

class ShapeImage(ABC):
    def __init__(self, w: int, h: int):
        self.w, self.h = w, h
    
    def label(self, obj_index: int = 0) -> str:
        x, y, w, h = self.xywh()
        return f"{obj_index} {x:.6f} {y:.6f} {w:.6f} {h:.6f}"

    @abstractmethod
    def xywh(self) -> tuple[float, float, float, float]:
        pass

    @abstractmethod
    def image(self) -> np.ndarray:
        pass

    @abstractmethod
    def describe(self) -> str:
        pass
