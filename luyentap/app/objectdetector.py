from ultralytics import YOLO

# Load model YOLOv8
model = YOLO("yolov8n.pt")

# Chạy detect bằng webcam (source=0 là camera mặc định)
model.predict(source=0, show=True)