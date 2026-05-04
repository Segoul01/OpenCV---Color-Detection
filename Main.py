# importing modules
import cv2
import os

# reading image
image_path = os.path.join('.', 'data', 'test-img.png')
img = cv2.imread(image_path)

# write image
cv2.imwrite(os.path.join('.', 'data', 'test-img-out.png'), img)

# visualizing image
cv2.imshow('image', img)
cv2.waitKey(0)  # NEED THIS ELSE WINDOW CLOSES IMMEDIATELY