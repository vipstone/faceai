# 表情识别 #
表情识别支持7种表情类型，生气、厌恶、恐惧、开心、难过、惊喜、平静等。

# 实现思路 #
使用OpenCV识别图片中的脸，在使用keras进行表情识别。

# 开发环境 #
- Windows10 x64
- python 3.6
- keras 2.1.6
- OpenCV 3.4.1


# 效果预览 #
![](https://raw.githubusercontent.com/vipstone/faceai/master/res/emotion.png)


# 实现代码 #

与[《性别识别》](https://github.com/vipstone/faceai/blob/master/doc/gender.md)相似，本文表情识别也是使用keras实现的，和性别识别相同，型数据使用的是[oarriaga/face_classification](https://github.com/oarriaga/face_classification)的，代码如下：

```
#coding=utf-8
#表情识别

import cv2
from keras.models import load_model
import numpy as np
import chineseText
import datetime

startTime = datetime.datetime.now()
emotion_classifier = load_model(
    'classifier/emotion_models/simple_CNN.530-0.65.hdf5')
endTime = datetime.datetime.now()
print(endTime - startTime)

emotion_labels = {
    0: '生气',
    1: '厌恶',
    2: '恐惧',
    3: '开心',
    4: '难过',
    5: '惊喜',
    6: '平静'
}

img = cv2.imread("img/emotion/emotion.png")
face_classifier = cv2.CascadeClassifier(
    "C:\Python36\Lib\site-packages\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml"
)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_classifier.detectMultiScale(
    gray, scaleFactor=1.2, minNeighbors=3, minSize=(40, 40))
color = (255, 0, 0)

for (x, y, w, h) in faces:
    gray_face = gray[(y):(y + h), (x):(x + w)]
    gray_face = cv2.resize(gray_face, (48, 48))
    gray_face = gray_face / 255.0
    gray_face = np.expand_dims(gray_face, 0)
    gray_face = np.expand_dims(gray_face, -1)
    emotion_label_arg = np.argmax(emotion_classifier.predict(gray_face))
    emotion = emotion_labels[emotion_label_arg]
    cv2.rectangle(img, (x + 10, y + 10), (x + h - 10, y + w - 10),
                  (255, 255, 255), 2)
    img = chineseText.cv2ImgAddText(img, emotion, x + h * 0.3, y, color, 20)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

```