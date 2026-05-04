# importing modules
import cv2
import os

# READING IMAGE
image_path = os.path.join('.', 'data', 'bird.jpg')
img = cv2.imread(image_path)

# write image
