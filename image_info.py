from ultralytics.models import YOLO
import numpy as np
import pandas as pd
from numpy.typing import NDArray
from ultralytics.engine.results import Boxes, BaseTensor, Results
from torch import Tensor
import math

BAGGAGE_CLASSES: list[str] = ["backpack","handbag","suitcase"]
COLUMNS: list[str] = ["x_center","y_center","width", "height","xmin","ymin","xmax","ymax","class_name","confidence"]

def get_ndarray(array: Tensor | NDArray) -> NDArray:
    if isinstance(array, Tensor):
        return array.cpu().numpy()
    return array


class ImageInfo:
    def __init__(self, img_path: str):
        """Create the ImageInfo instance from a path to an image file. Use the yolov8m-seg model internally"""
        self.__build_df(img_path)

    def __build_df(self, img_path: str) -> None:
        model: YOLO = YOLO("yolov8m-seg.pt")
        result: list[Results] = model(img_path)
        if result and result[0].boxes:
            boxes: Boxes = result[0].boxes
            xywhn: NDArray = get_ndarray(boxes.xywhn)
            xyxy: NDArray = get_ndarray(boxes.xyxy)
            class_ids: NDArray = get_ndarray(boxes.cls)
            conf: NDArray = get_ndarray(boxes.conf)
            names: dict[int, str] = result[0].names

            df_xywh: pd.DataFrame = pd.DataFrame(xywhn, columns=["x_center", "y_center", "width", "height"])
            df_xyxy: pd.DataFrame = pd.DataFrame(xyxy, columns=["xmin", "ymin", "xmax", "ymax"])
            self.df: pd.DataFrame = pd.concat([df_xywh, df_xyxy], axis=1)
            self.df["class_name"] = [names[class_id] for class_id in class_ids]
            self.df["confidence"] = conf
        else:
            self.df = pd.DataFrame(columns=COLUMNS)

    def __len__(self) -> int:
        return len(self.df)
    
    def __indices_by_class_list(self, classes: list[str]) -> list[int]:
        return self.df.index[self.df.class_name.isin(classes)].to_list()

    def boxesClass(self, class_name: str) -> list[int]:
        """Get a list of indices of the objects of a  class_name class"""
        return self.__indices_by_class_list([class_name])
    
    def baggage_indices(self) -> list[int]:
        """Get a list of indices of the baggage objects"""
        return self.__indices_by_class_list(BAGGAGE_CLASSES)
    
    def boxInfo(self, box_index) -> tuple:
        """Get a list of absolute coordinates of the object with the box_index index, along with confidence level and the object class name"""
        row: pd.Series = self.df.loc[box_index].loc[["xmin","ymin","xmax","ymax","confidence","class_name"]]
        *numbers, class_name = row
        return tuple([float(x) for x in numbers] + [class_name])
    
    def dataFrame(self) -> pd.DataFrame:
        """Get a DataFrame with a comprehensive data about all the objects, found in the image"""
        return self.df
    
    def relative_center(self, box_index) -> tuple[float,...]:
        """Get relative coordinates of the center of the specific object indexed with box_index"""
        row: pd.Series = self.df.loc[box_index].loc[["x_center","y_center"]]
        return tuple(float(x) for x in row)
    
    def distance(self, index_one, index_two) -> float:
        """Get a relative distance between two objects with the specified indices"""
        x1, y1 = self.relative_center(index_one)
        x2, y2 = self.relative_center(index_two)
        dx, dy = x2 - x1, y2 - y1
        return math.sqrt(dx * dx + dy * dy)

    def suitcaseHandbagPerson(self, max_distance: float = 1) -> dict[int, tuple[int, float] | None]:
        """Get the dictionary, containing data about all baggage pieces and respective closest persons.
        If the distance to the closest person exceeds the max_distance threshold return None instead of the person data.
        The max_distance value is relative to the image size, and is expected to be between 0 and 1.
        """
        baggage_data: dict[int, tuple[int, float] | None] = dict.fromkeys(self.baggage_indices())
        person_indices: list[int] = self.boxesClass("person")
        if person_indices:
            for bag in baggage_data:
                distance, person_idx = min((self.distance(bag, p), p) for p in person_indices)
                baggage_data[bag] = None if distance > max_distance else (person_idx, distance)
        
        return baggage_data

if __name__ == "__main__":
    ii: ImageInfo = ImageInfo("./bag.jpg")
    print(f"LENGTH: {len(ii)}")
    print(ii.boxesClass("person"))
    print(f"DataFrame: {ii.dataFrame()}")
    print("BoxInfo: ", ii.boxInfo(0))
    print("COORD: ", ii.relative_center(0), ii.relative_center(1))
    print("DISTANCE: ", ii.distance(0, 1))
    print(f"Dict: {ii.suitcaseHandbagPerson(1.0)}")

    empty: ImageInfo = ImageInfo("./empty.jpg")
    print(f"LENGTH: {len(empty)}")
    print(f"EMPTY DataFrame: {empty.dataFrame()}")
    print(f"EMPTY Dict: {empty.suitcaseHandbagPerson(1.0)}")
    print(f"EMPTY persons: {empty.boxesClass("person")}")
    print(f"EMPTY bags: {empty.baggage_indices()}")
