# 图片人脸检测（dlib版）

本文为dlib版的图片人脸检测，区别于OpenCV版的人脸检测，点击[查看OpenCV版](https://github.com/vipstone/faceai/blob/master/doc/detectionOpenCV.md)的。

## dlib与OpenCV对比 ##
人脸识别进准度，dlib > OpenCV

## 安装dlib ##

下载地址：[https://pypi.org/simple/dlib/](https://pypi.org/simple/dlib/) 选择适合你的版本，本人配置：

> Window 10 + Python 3.6.4

我现在的版本是：dlib-19.8.1-cp36-cp36m-win_amd64.whl

使用命令安装：
>pip3 install D:\soft\py\dlib-19.8.1-cp36-cp36m-win_amd64.whl

显示结果：
Processing d:\soft\py\dlib-19.8.1-cp36-cp36m-win_amd64.whl
Installing collected packages: dlib
Successfully installed dlib-19.8.1

为安装成功。

## 下载训练模型 ##
训练模型用于是人脸识别的关键，用于查找图片的关键点。

下载地址：[http://dlib.net/files/](http://dlib.net/files/)

下载文件：shape_predictor_68_face_landmarks.dat.bz2

当然你也可以训练自己的人脸关键点模型，这个功能会放在后面讲。

下载好的模型文件，我的存放地址是：C:\Python36\Lib\site-packages\dlib-data\shape_predictor_68_face_landmarks.dat.bz2

解压：shape_predictor_68_face_landmarks.dat.bz2得到文件：shape_predictor_68_face_landmarks.dat


## 代码实现 ##
```
#coding=utf-8

import cv2
import dlib

path = "img/meinv.png"
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#人脸分类器
detector = dlib.get_frontal_face_detector()
# 获取人脸检测器
predictor = dlib.shape_predictor(
    "C:\\Python36\\Lib\\site-packages\\dlib-data\\shape_predictor_68_face_landmarks.dat"
)

dets = detector(gray, 1)
for face in dets:
    shape = predictor(img, face)  # 寻找人脸的68个标定点
    # 遍历所有点，打印出其坐标，并圈出来
    for pt in shape.parts():
        pt_pos = (pt.x, pt.y)
        cv2.circle(img, pt_pos, 2, (0, 255, 0), 1)
    cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

