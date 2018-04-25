# 人脸识别

人脸识别，需要使用face_recognition库做人脸对比，OpenCV获取摄像头数据。

## 环境 ##
+   Windows 10 
+   OpenCV 3.4.1
+   Dlib 19.8.1
+   face_recognition 1.2.2


## 环境安装 ##

**OpenCV安装**

点击查看：[《OpenCV环境搭建》](https://github.com/vipstone/faceai/blob/master/doc/settingup.md)

**Dlib安装**

点击查看：[《图片人脸检测（dlib版）》](https://github.com/vipstone/faceai/blob/master/doc/detectionDlib.md)

**face_recognition安装**

使用命令：
>pip3 install face_recognition


此项，安装需要很长时间。

## 效果预览 ##
![](https://raw.githubusercontent.com/vipstone/faceai/master/res/faceRecognition.gif)


## 完整代码 ##

```
#coding=utf-8
#人脸识别类 - 使用face_recognition模块
import cv2
import face_recognition
import os

path = "img/face_recognition"  # 模型数据图片目录
cap = cv2.VideoCapture(0)
total_image_name = []
total_face_encoding = []
for fn in os.listdir(path):  #fn 表示的是文件名q
    print(path + "/" + fn)
    total_face_encoding.append(
        face_recognition.face_encodings(
            face_recognition.load_image_file(path + "/" + fn))[0])
    fn = fn[:(len(fn) - 4)]  #截取图片名（这里应该把images文件中的图片名命名为为人物名）
    total_image_name.append(fn)  #图片名字列表
while (1):
    ret, frame = cap.read()
    # 发现在视频帧所有的脸和face_enqcodings
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    # 在这个视频帧中循环遍历每个人脸
    for (top, right, bottom, left), face_encoding in zip(
            face_locations, face_encodings):
        # 看看面部是否与已知人脸相匹配。
        for i, v in enumerate(total_face_encoding):
            match = face_recognition.compare_faces(
                [v], face_encoding, tolerance=0.5)
            name = "Unknown"
            if match[0]:
                name = total_image_name[i]
                break
        # 画出一个框，框住脸
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # 画出一个带名字的标签，放在框下
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255),
                      cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0,
                    (255, 255, 255), 1)
    # 显示结果图像
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```