import numpy as np

class ShapeImage:
    def __init__(self):
        raise NotImplementedError()
    
    def image(self) -> np.ndarray:
        raise NotImplementedError()
    
    def label(self, obj_index: int = 0) -> str:
        raise NotImplementedError()
    
    def describe(self) -> str:
        raise NotImplementedError()
    