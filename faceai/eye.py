#coding=utf-8
# 38x-37x 44x-43x
# 40x-39x 46x-45x

import cv2
import dlib
import numpy as np

path = "img/eye-2.png"
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor(
#     "C:\\Python36\\Lib\\site-packages\\dlib-data\\shape_predictor_68_face_landmarks.dat"
# )

# dets = detector(gray, 1)
# for face in dets:
#     shape = predictor(img, face)

#     leftDiffer1 = shape.parts()[37].x - shape.parts()[36].x
#     leftDiffer2 = shape.parts()[39].x - shape.parts()[38].x

#     print("leftDiffer1:{} leftDiffer2:{} ".format(leftDiffer1, leftDiffer2))

# classifier = cv2.CascadeClassifier(
#     "C:\Python36\Lib\site-packages\opencv-master\data\haarcascades\haarcascade_eye_tree_eyeglasses.xml"  #haarcascade_eye
# )
# img = cv2.imread(path, 0)
# gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# faceRects = classifier.detectMultiScale(
#     gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
# if len(faceRects):
#     for faceRect in faceRects:
#         x, y, w, h = faceRect
#         cv2.rectangle(img, (x, y), (x + h, y + w), (255, 0, 0), 2)
#         rightEyeImg = gray[(y):(y + h), (x):(x + w)]

# cv2.imshow('img', rightEyeImg)

# eyeImg = img[(y):(y + h), (x):(x + w)]
# eyeImg = cv2.medianBlur(eyeImg, 5)
# cimg = cv2.cvtColor(eyeImg, cv2.COLOR_GRAY2BGR)

# circles = cv2.HoughCircles(
#     eyeImg,
#     cv2.HOUGH_GRADIENT,
#     1,
#     20,
#     param1=50,
#     param2=30,
#     minRadius=0,
#     maxRadius=0)

# circles = np.uint16(np.around(circles))
# for i in circles[0, :]:
#     # draw the outer circle
#     cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
#     # draw the center of the circle
#     cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

# cv2.imshow('detected circles', cimg)

# cv2.imshow("image", img)  # 显示图像

# cv2.waitKey(0)
# cv2.destroyAllWindows()

img = cv2.imread(path, 0)
img = cv2.medianBlur(img, 3)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(
    img,
    cv2.HOUGH_GRADIENT,
    1,
    50,
    param1=50 / 5,
    param2=30 / 5,
    minRadius=0,
    maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('detected circles', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()