import cv2
import numpy as np

path = "image.png"
img = cv2.imread(path)
height, width, depth = img.shape[0:3]
thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))
kernel = np.ones((3, 3), np.uint8)

hi_mask = cv2.dilate(thresh, kernel, iterations=1)
specular = cv2.inpaint(img, hi_mask, 5, flags = cv2.INPAINT_TELEA)
cv2.namedWindow("Image", 0)
cv2.resizeWindow("Image", int(width / 2), int(height / 2))
cv2.imshow("Image", img)
cv2.namedWindow("newImage", 0)
cv2.resizeWindow("newImage", int(width / 2), int(height / 2))
a = cv2.imshow("newImage", specular)
cv2.imwrite("43.jpg", specular)
cv2.waitKey(0)
cv2.destroyAllWindows()

