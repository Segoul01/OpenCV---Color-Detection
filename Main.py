# importing modules
import cv2
from PIL import Image
from util import get_limits


# Reading Webcam
webcam = cv2.VideoCapture(0)

color = [0, 255, 0]
# Visualizing Webcam
while True:
    ret, frame = webcam.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=color)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)

    cv2.imshow('Mask', mask)
    cv2.imshow("Webcam", frame)
    if (cv2.waitKey(20) & 0xFF == ord('q')):
        break


webcam.release()
cv2.destroyAllWindows()

# # Reading Video
# video_path = os.path.join('.', 'data', 'vid.mp4')
# video = cv2.VideoCapture(video_path)


# # Visualizing Video
# ret = True
# while ret:
#     ret, frame = video.read()

#     # Displaying the frame
#     cv2.imshow('video', frame)
#     cv2.waitKey(33)

# video.release()
# cv2.destroyAllWindows()

# # reading image
# image_path = os.path.join('.', 'data', 'test-img.png')
# img = cv2.imread(image_path)

# # write image
# cv2.imwrite(os.path.join('.', 'data', 'test-img-out.png'), img)

# # visualizing image
# cv2.imshow('image', img)
# cv2.waitKey(0)  # NEED THIS ELSE WINDOW CLOSES IMMEDIATELY