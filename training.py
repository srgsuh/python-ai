from ultralytics.models import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8m.pt")
    model.train(data="./datasets/data.yaml", batch=2, epochs=30, imgsz=256, name="circle_rect")