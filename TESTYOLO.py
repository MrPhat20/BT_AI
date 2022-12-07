import cv2
import torch
from PIL import Image

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

im1 = Image.open('xe-bus-anh-hoang-trieu12-16189728901651645284076.jpg') 
im2 = cv2.imread('anh-xe-buyt-82.jpg')[..., ::-1] 

results = model([im1, im2], size=640)

results.print()  
results.save() 

results.xyxy[0]  
results.pandas().xyxy[0]  
