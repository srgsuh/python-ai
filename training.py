from ultralytics.models import YOLO

model = YOLO("yolov8m.pt")
model.train(data="./datasets/data.yaml", batch=2, epochs=5, imgsz=256, name="circle_find")