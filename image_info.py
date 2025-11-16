from ultralytics.models import YOLO
import numpy as np
import pandas as pd
from numpy.typing import NDArray
from ultralytics.engine.results import Boxes, BaseTensor
import math

BAGGAGE_CLASSES: list[str] = ["backpack","handbag","suitcase"]

class ImageInfo:
    def __init__(self, img_path: str):
        """Create the ImageInfo instance from a path to an image file. Use the yolov8m-seg model internally"""
        model: YOLO = YOLO("yolov8m-seg.pt")
        results: list[BaseTensor] = model(img_path)
        
        xywhn: NDArray = results[0].boxes.xywhn.cpu().numpy()
        xyxy: NDArray = results[0].boxes.xyxy.cpu().numpy()
        ids: NDArray = results[0].boxes.cls.cpu().numpy()
        conf: NDArray = results[0].boxes.conf.cpu().numpy()

        df_xywh: pd.DataFrame = pd.DataFrame(xywhn, columns=["x_center", "y_center", "width", "height"])
        df_xyxy: pd.DataFrame = pd.DataFrame(xyxy, columns=["xmin", "ymin", "xmax", "ymax"])
        self.df: pd.DataFrame = pd.concat([df_xywh, df_xyxy], axis=1)
        self.df["class_name"] = [results[0].names[class_id] for class_id in ids]
        self.df["confidence"] = conf

    def __indices_by_class_list(self, classes: list[str]) -> list[int]:
        return self.df.index[self.df.class_name.isin(classes)].to_list()

    def boxesClass(self, class_name: str) -> list[int]:
        """Get a list of indices of the objects of a  class_name class"""
        return self.__indices_by_class_list([class_name])
    
    def baggage_indices(self) -> list[int]:
        """Get a list of indices of the baggage objects"""
        return self.__indices_by_class_list(BAGGAGE_CLASSES)
    
    def boxInfo(self, box_index) -> tuple:
        """Get list of absolute coordinates of the object with the box_index index, along with confidence level and the object class name"""
        row: pd.Series = self.df.loc[box_index].loc[["xmin","ymin","xmax","ymax","confidence","class_name"]]
        *numbers, class_name = row
        return tuple(float(x) for x in numbers) + (str(class_name),)
    
    def dataFrame(self) -> pd.DataFrame:
        """Get the DataFrame with a comprehensive data about all the objects, found in the image"""
        return self.df
    
    def relative_center(self, box_index) -> tuple[float,...]:
        """Get relative coordinates of the center of the specific object indexed with box_index"""
        row: pd.Series = self.df.loc[box_index].loc[["x_center","y_center"]]
        return tuple(float(x) for x in row)
    
    def distance(self, index_one, index_two) -> float:
        """Get relative distance between the two objects with certain indices"""
        x1, y1 = self.relative_center(index_one)
        x2, y2 = self.relative_center(index_two)

        return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

    def suitcaseHandbagPerson(self, max_distance: float = 1) -> dict[int, tuple[int, float] | None]:
        """Get the dictionary, containing data about all baggage pieces and respective closest persons.
        If the distance to the closest person exceeds the max_distance threshold return None instead of the person data.
        The max_distance value is relative to the image size, and is expected to be between 0 and 1.
        """
        distances: dict[int, tuple[int, float] | None] = {bag_idx: None for bag_idx in self.baggage_indices()}
        person_indices = self.boxesClass("person")
        if person_indices:
            for bag_idx in distances:
                distance, person_idx = min((self.distance(bag_idx, p_idx), p_idx) for p_idx in person_indices)
                distances[bag_idx] = None if distance > max_distance else (person_idx, distance)
        
        return distances

if __name__ == "__main__":
    ii: ImageInfo = ImageInfo("./lonely_bag.jpg")
    print(ii.boxesClass("person"))
    print("BoxInfo: ", ii.boxInfo(0))
    print("COORD: ", ii.relative_center(0), ii.relative_center(1))
    print("DISTANCE: ", ii.distance(0, 1))
    print(f"Dict: {ii.suitcaseHandbagPerson(1.0)}")