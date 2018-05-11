import cv2
import dlib
import numpy as np
import time

classifier = cv2.CascadeClassifier(
    "C:\Python36\Lib\site-packages\opencv-master\data\haarcascades\haarcascade_eye_tree_eyeglasses.xml"  # haarcascade_eye
)


#彩色直方图均衡化
def hist(img):
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    channels = cv2.split(ycrcb)
    cv2.equalizeHist(channels[0], channels[0])  #输入通道、输出通道矩阵
    cv2.merge(channels, ycrcb)  #合并结果通道
    cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)
    return img


def discern(img):
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceRects = classifier.detectMultiScale(
        grayImg, scaleFactor=1.2, minNeighbors=3, minSize=(30, 30))
    if len(faceRects):
        for faceRect in faceRects:
            x, y, w, h = faceRect
            rightEyeImg = img[(y):(y + h), (x):(x + w)]
            # cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
            # rightEyeImg = hist(rightEyeImg)
            rightEyeImg = cv2.GaussianBlur(rightEyeImg, (5, 5), 1)

            cv2.imwrite("img/temp.png", rightEyeImg)
            # cv2.imshow("img", rightEyeImg)
    # print(len(faceRects))


# discern(cv2.imread("img/ag-2.png"))

img = cv2.imread("img/temp.png", 0)

# img = cv2.GaussianBlur(img, (3, 3), 0)
# img = cv2.Canny(img, 50, 150)
img = cv2.bilateralFilter(img, 7, 50, 50)

# x = cv2.Sobel(img, -1, 1, 0, ksize=3)
# y = cv2.Sobel(img, -1, 0, 1, ksize=3)
# absx = cv2.convertScaleAbs(x)
# absy = cv2.convertScaleAbs(y)
# dist = cv2.addWeighted(absx, 0.5, absy, 0.5, 0)

# img = cv2.GaussianBlur(img, (5, 5), 1)

# laplacian = cv2.Laplacian(img, -1, ksize=3)

# laplacian = cv2.GaussianBlur(laplacian, (3, 3), 1)
# laplacian = cv2.medianBlur(laplacian, 3)

# img = dist

# img = cv2.cvtColor(dist, cv2.COLOR_BGR2GRAY)

cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # cv2.imread("img/temp.png")  #

# cv2.imshow("img2", img)
# cv2.imshow("grayimg", grayimg)

circles = cv2.HoughCircles(
    img,
    cv2.HOUGH_GRADIENT,
    1,
    100,
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
cv2.imshow("img", cimg)

cv2.waitKey(0)
cv2.destroyAllWindows()