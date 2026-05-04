# importing modules
import cv2
import os

# Reading Video
video_path = os.path.join('.', 'data', 'vid.mp4')
video = cv2.VideoCapture(video_path)


# Visualizing Video
ret = True
while ret:
    ret, frame = video.read()

    # Displaying the frame
    cv2.imshow('video', frame)
    cv2.waitKey(33)

video.release()
cv2.destroyAllWindows()

# # reading image
# image_path = os.path.join('.', 'data', 'test-img.png')
# img = cv2.imread(image_path)

# # write image
# cv2.imwrite(os.path.join('.', 'data', 'test-img-out.png'), img)

# # visualizing image
# cv2.imshow('image', img)
# cv2.waitKey(0)  # NEED THIS ELSE WINDOW CLOSES IMMEDIATELY