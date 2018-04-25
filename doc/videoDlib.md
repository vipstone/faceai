# 视频人脸检测（dlib版）

视频人脸检测是图片识别的高级版本，图片检测详情点击查看我的上一篇[《图片人脸检测（dlib版）》](https://github.com/vipstone/faceai/blob/master/doc/detectionDlib.md) 

除了人脸识别用的是Dlib外，还是用OpenCV读取摄像头和处理图片（转为灰色），所以给出相关的文档，方便理解。

[视频人脸检测（OpenCV版）](doc/videoOpenCV.md)

有了OpenCV的视频人脸检测，Dlib也大致相同除了视频识别器模型的声明和使用不同，具体的细节请参考，[视频人脸检测（OpenCV版）](doc/videoOpenCV.md) 那篇已经讲的很细致了，在这就不具体叙述了。

完整的代码如下：
```
# coding=utf-8
import cv2
import dlib

detector = dlib.get_frontal_face_detector()  #使用默认的人类识别器模型


def discern(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(gray, 1)
    for face in dets:
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.imshow("image", img)


cap = cv2.VideoCapture(0)
while (1):
    ret, img = cap.read()
    discern(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

```

那么，OpenCV和Dlib的视频识别对比，有两个地方是不同的：

1.Dlib模型识别的准确率和效果要好于OpenCV；

2.Dlib识别的性能要比OpenCV差，使用视频测试的时候Dlib有明显的卡顿，但是OpenCV就好很多，基本看不出来；