#coding=utf-8
#图片修复

import cv2
import numpy as np

path = "img/inpaint.png"

img = cv2.imread(path)
hight, width, depth = img.shape[0:3]

thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
hi_mask = cv2.dilate(thresh, kernel, iterations=3)
specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)

cv2.namedWindow("Image", 0)
cv2.resizeWindow("Image", int(width / 2), int(hight / 2))
cv2.imshow("Image", img)

cv2.namedWindow("newImage", 0)
cv2.resizeWindow("newImage", int(width / 2), int(hight / 2))
cv2.imshow("newImage", specular)
cv2.waitKey(0)
cv2.destroyAllWindows()