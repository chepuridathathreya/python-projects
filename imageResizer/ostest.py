import os
import cv2

print("Current folder:", os.getcwd())
print("Files here:", os.listdir())

image = cv2.imread("original.png")

print(image)