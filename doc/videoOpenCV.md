# 视频人脸检测（OpenCV版）

视频人脸检测是图片人脸检测的高级版本，图片检测详情点击查看我的上一篇[《图片人脸检测（OpenCV版）》](https://github.com/vipstone/faceai/blob/master/doc/detectionOpenCV.md) 。

**实现思路：**
调用电脑的摄像头，把摄像的信息逐帧分解成图片，基于图片检测标识出人脸的位置，把处理的图片逐帧绘制给用户，用户看到的效果就是视频的人脸检测。

效果预览：

![](https://raw.githubusercontent.com/vipstone/faceai/master/res/video-jiance.gif)

## 实现步骤 ##

使用OpenCV调用摄像头并展示。

**获取摄像头**
```
cap = cv2.VideoCapture(0)
```
参数0表示，获取第一个摄像头。

**显示摄像头**
逐帧显示，代码如下：
```
while (1): 
    ret, img = cap.read()
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()  # 释放摄像头
cv2.destroyAllWindows()  # 释放窗口资源
```

cv2.waitKey(1) & 0xFF使用了“&”位元算法，含义是获取用户输入的最后一个字符的ASCII码，如果输入的是“q”，则跳出循环。

**视频的人脸识别**

这个时候，用到了上一节的[《图片人脸检测（OpenCV版）》](https://github.com/vipstone/faceai/blob/master/doc/detectionOpenCV.md) 把人脸识别的代码封装成方法，代码如下：
```
def discern(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cap = cv2.CascadeClassifier(
        "C:\Python36\Lib\site-packages\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml"
    )
    faceRects = cap.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50))
    if len(faceRects):
        for faceRect in faceRects:
            x, y, w, h = faceRect
            cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 2)  # 框出人脸
    cv2.imshow("Image", img)
```

再循环摄像头帧图片的时候，调用图片识别方法即可，代码如下：
```
# 获取摄像头0表示第一个摄像头
cap = cv2.VideoCapture(0)
while (1):  # 逐帧显示
    ret, img = cap.read()
    # cv2.imshow("Image", img)
    discern(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()  # 释放摄像头
cv2.destroyAllWindows()  # 释放窗口资源
```

完整的代码如下：
```
# -*- coding:utf-8 -*-
# OpenCV版本的视频检测
import cv2


# 图片识别方法封装
def discern(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cap = cv2.CascadeClassifier(
        "C:\Python36\Lib\site-packages\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml"
    )
    faceRects = cap.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50))
    if len(faceRects):
        for faceRect in faceRects:
            x, y, w, h = faceRect
            cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 2)  # 框出人脸
    cv2.imshow("Image", img)


# 获取摄像头0表示第一个摄像头
cap = cv2.VideoCapture(0)
while (1):  # 逐帧显示
    ret, img = cap.read()
    # cv2.imshow("Image", img)
    discern(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()  # 释放摄像头
cv2.destroyAllWindows()  # 释放窗口资源

```

