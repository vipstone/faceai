# FaceAI

一款优秀的人脸、视频、文字：检测、识别的智能AI项目。

**开发环境**

>Windows 10（x64）
>
>Python 3.6.4
>
>OpenCV 3.4.1
>
>Dlib 19.8.1
>
>face_recognition 1.2.2
>
>Tesseract OCR 4.0.0-beta.1
>

## 技术实现方案 ##

相应技术使用模块

	人脸识别：OpenCV / Dlib

	人脸检测：face_recognition
	
	视频识别：OpenCV + face_recognition

	文字识别：Tesseract OCR


## 教程文档 ##

[OpenCV环境搭建](doc/settingup.md)

[Tesseract OCR文字识别](doc/tesseractOCR.md)

[图片人脸检测（OpenCV版）](doc/detectionOpenCV.md)

[图片人脸检测（Dlib版）](doc/detectionDlib.md)

[视频人脸检测（OpenCV版）](doc/videoOpenCV.md)

[视频人脸检测（Dlib版）](doc/videoDlib.md)

[脸部轮廓绘制](doc/faceRecognitionOutline.md)

[数字化妆](doc/faceRecognitionMakeup.md)

[视频人脸识别](doc/faceRecognition.md)

[头像特效合成](doc/compose.md)

## 功能预览 ##

**绘制脸部轮廓**

<img src="https://raw.githubusercontent.com/vipstone/faceai/master/res/face_recognition-outline.png" width = "250" height = "300" alt="绘制脸部轮廓" />

----------

**人脸68个关键点标识**

<img src="https://raw.githubusercontent.com/vipstone/faceai/master/res/dlib68.png" width = "230" height = "300" alt="人脸68个关键点标识" />

----------

**头像特效合成**

<img src="https://raw.githubusercontent.com/vipstone/faceai/master/res/compose.png" width = "200" height = "300" alt="头像特效合成"  />

----------

**数字化妆**

<img src="https://raw.githubusercontent.com/vipstone/faceai/master/res/faceRecognitionMakeup.png" width = "230" height = "300" alt="视频人脸识别"  />

----------

**视频人脸检测**

![](https://raw.githubusercontent.com/vipstone/faceai/master/res/video-jiance.gif)

----------

**视频人脸识别**

![](https://raw.githubusercontent.com/vipstone/faceai/master/res/faceRecognition.gif)



## TODO ##

笑脸检测

眼睛移动方向检测

性别检测

OpenCV + Tensorflow模型的人脸识别

Dlib性能优化方案

Dlib模型训练方法

Tesseract模型训练方法



