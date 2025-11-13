from ultralytics.models import YOLO

DEFAULT_MODEL = "yolov8m-seg.pt"
MODELS = ["yolov8m-seg.pt"]

CLASSES: dict[str, str] = {
    "0": "person",
    "24": "backpack",
    "26": "handbag",
    "28": "suitcase"
}

class ImageInfo:
    def __init__(self, img_path: str, model_name: str = DEFAULT_MODEL):
        if model_name not in [MODELS]:
            raise ValueError(f"Unacceptable model name: {model_name}")
        self.__model = YOLO(model_name)