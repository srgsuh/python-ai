from ultralytics.models import YOLO
import numpy as np
from numpy.typing import NDArray
from ultralytics.engine.results import Boxes, BaseTensor

BAGGAGE_CLASSES: dict[str, str] = {
    "24": "backpack",
    "26": "handbag",
    "28": "suitcase"
}

class ImageInfo:
    def __init__(self, img_path: str):
        self.__model = YOLO("yolov8m-seg.pt")
        results: list[BaseTensor] = self.__model(img_path)
        self.boxes: BaseTensor  = results[0].boxes.cpu()
        self.ids = results[0].boxes.cls.cpu().numpy()
        self.class_by_id: dict[int, str] = results[0].names
        self.id_by_class: dict[str, int] = {value: key for key, value in self.class_by_id.items()}
    
    def boxesClass(self, class_name: str) -> list[int]:
        class_id = self.id_by_class[class_name]
        indices = np.nonzero(self.ids == class_id)[0]
        return indices.tolist()
    
    def boxInfo(self, box_index):
        raise NotImplementedError()
    
if __name__ == "__main__":
    ii: ImageInfo = ImageInfo("./bus.jpg")
    print(ii.boxesClass("person"))