from ultralytics import YOLO

model = YOLO('runs/detect/train/weights/best.pt')
result = model.predict(source='fish.jpg', show= False, save = True)

results=