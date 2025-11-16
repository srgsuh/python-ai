from ultralytics.models import YOLO
import numpy as np
import pandas as pd
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
        self.xywh = results[0].boxes.xywh.cpu().numpy()
        self.xyxy = results[0].boxes.xyxy.cpu().numpy()
        self.conf = results[0].boxes.conf.cpu().numpy()
        self.class_by_id: dict[int, str] = results[0].names
        self.id_by_class: dict[str, int] = {value: key for key, value in self.class_by_id.items()}
        self.__build_data_frame()
    
    def __build_data_frame(self) -> None:
        df_xywh: pd.DataFrame = pd.DataFrame(self.xywh, columns=["x_center", "y_center", "width", "height"])
        df_xyxy: pd.DataFrame = pd.DataFrame(self.xyxy, columns=["xmin", "ymin", "xmax", "ymax"])
        self.df: pd.DataFrame = pd.concat([df_xywh, df_xyxy], axis=1)
        self.df["class_name"] = [self.class_by_id[class_id] for class_id in self.ids]
        self.df["confidence"] = self.conf
        print(self.df)

    def boxesClass(self, class_name: str) -> list[int]:
        return self.df.index[self.df.class_name == class_name].to_list()
    
    def boxInfo(self, box_index) -> tuple:
        row: pd.Series = self.df.loc[box_index].loc[["xmin","ymin","xmax","ymax","confidence","class_name"]]
        *numbers, class_name = row
        return tuple(float(x) for x in numbers) + (str(class_name),)
    
    def dataFrame(self) -> pd.DataFrame:
        return self.df

if __name__ == "__main__":
    ii: ImageInfo = ImageInfo("./bus.jpg")
    print(ii.boxesClass("person"))
    print("BoxInfo: ", ii.boxInfo(0))