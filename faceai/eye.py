#coding=utf-8
# 38x-37x 44x-43x
# 40x-39x 46x-45x

import cv2
import dlib
import numpy as np
import time

# img = cv2.imread(path)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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

counter = 1


#获取眼球中心
def houghCircles(path, counter):
    img = cv2.imread(path, 0)
    # img = cv2.medianBlur(img, 5)

    x = cv2.Sobel(img, -1, 1, 0, ksize=3)
    y = cv2.Sobel(img, -1, 0, 1, ksize=3)
    absx = cv2.convertScaleAbs(x)
    absy = cv2.convertScaleAbs(y)
    img = cv2.addWeighted(absx, 0.5, absy, 0.5, 0)

    # ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    # channels = cv2.split(ycrcb)
    # cv2.equalizeHist(channels[0], channels[0])  #输入通道、输出通道矩阵
    # cv2.merge(channels, ycrcb)  #合并结果通道
    # cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)

    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # cv2.imshow("img2", img)
    # cv2.imshow("grayimg", grayimg)

    circles = cv2.HoughCircles(
        img,
        cv2.HOUGH_GRADIENT,
        1,
        50,
        param1=50,
        param2=10,
        minRadius=2,
        maxRadius=0)

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        # cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 1)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 2)
    # cv2.imshow("img" + str(counter), cimg)
    return (i[0] + 3, i[1] + 3)


#彩色直方图均衡化
def hist(img):
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    channels = cv2.split(ycrcb)
    cv2.equalizeHist(channels[0], channels[0])  #输入通道、输出通道矩阵
    cv2.merge(channels, ycrcb)  #合并结果通道
    cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)
    return img


classifier = cv2.CascadeClassifier(
    "C:\Python36\Lib\site-packages\opencv-master\data\haarcascades\haarcascade_eye.xml"  #haarcascade_eye_tree_eyeglasses
)


def discern(img, counter):
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    color = (0, 255, 0)
    faceRects = classifier.detectMultiScale(
        grayImg, scaleFactor=1.2, minNeighbors=3, minSize=(58, 58))
    if len(faceRects):
        for faceRect in faceRects:
            x, y, w, h = faceRect
            rightEyeImg = img[(y):(y + h), (x):(x + w)]
            # cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
            rightEyeImg = cv2.GaussianBlur(rightEyeImg, (5, 5), 1)
            # rightEyeImg = hist(rightEyeImg)
            cv2.imwrite("img/temp.png", rightEyeImg)
            # cv2.imwrite("img/temp.png", rightEyeImg)
            circleCenter = houghCircles("img/temp.png", counter)  #(x,y)
            cv2.circle(img, (x + circleCenter[0], y + circleCenter[1]), 2,
                       (128, 0, 0), 2)
            counter += 1
        cv2.imshow("image", img)


# path = "img/ag-3.png"
# img = cv2.imread(path)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faceRects = classifier.detectMultiScale(
#     gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
# if len(faceRects):
#     for faceRect in faceRects:
#         x, y, w, h = faceRect
#         # cv2.rectangle(img, (x, y), (x + h, y + w), (255, 0, 0), 2)
#         rightEyeImg = img[(y):(y + h), (x):(x + w)]
#         cv2.imwrite("img/temp.png", rightEyeImg)
#         houghCircles("img/temp.png", counter)
#         counter += 1
#         # cv2.imshow("img", houghCircles("img/temp.png"))

path = "img/ag.png"
img = cv2.imread(path)
discern(img, counter)

# cap = cv2.VideoCapture(0)
# while (1):
#     ret, frame = cap.read()

#     # cv2.imshow('frame', gray)
#     discern(frame, counter)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#

# cv2.imwrite('img/eye-2.png', rightEyeImg)

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

# time.sleep(1)

# img = cv2.imread("img/eye-2.png")
# ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
# channels = cv2.split(ycrcb)
# cv2.equalizeHist(channels[0], channels[0])  #输入通道、输出通道矩阵
# cv2.merge(channels, ycrcb)  #合并结果通道
# cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)
# # cv2.imshow("old image", cv2.imread("img/hist.png"))
# # cv2.imshow("image", img)

# cv2.imwrite("img/eye-3.png", img)

# time.sleep(1)

# cv2.imshow('detected circles', cimg)

cv2.waitKey(0)
cv2.destroyAllWindows()