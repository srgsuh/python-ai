from ultralytics.models import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8m.pt")
    model.train(data="./datasets/data.yaml", epochs=5, imgsz=256, batch=2, name="shapes")