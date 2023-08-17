import torch
from ultralytics import YOLO

print(torch.cuda.is_available())
print('==========================')
# print(ultralytics.checks())


model = YOLO('yolov8n.pt')

model.train(data = 'c:/yolov8/Fish-44/data.yaml', imgsz= 640, epoch= 30 )