#coding=utf-8
#图片检测 - OpenCV版本
import cv2
import datetime
import time

filepath = "img/xingye-1.png"
# OpenCV人脸识别分类器
classifier = cv2.CascadeClassifier(
    "C:\Python36\Lib\site-packages\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml"
)

# 程序开始时间
startTime = datetime.datetime.now()

img = cv2.imread(filepath)  # 读取图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换灰色
color = (0, 255, 0)  # 定义绘制颜色
# 调用识别人脸
faceRects = classifier.detectMultiScale(
    gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
if len(faceRects):  # 大于0则检测到人脸
    for faceRect in faceRects:  # 单独框出每一张人脸
        x, y, w, h = faceRect
        # 框出人脸
        cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
        # 左眼
        cv2.circle(img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
        #右眼
        cv2.circle(img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
        #嘴巴
        cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                      (x + 5 * w // 8, y + 7 * h // 8), color)

# 程序结束时间
endTime = datetime.datetime.now()
print((endTime - startTime))
cv2.imshow("image", img)  # 显示图像
cv2.waitKey(0)
cv2.destroyAllWindows()
