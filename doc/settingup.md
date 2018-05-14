# 环境搭建 #

环境搭建为OpenCV的python（一下简称py）开发环境搭建，建立在py3的环境和语法上实现的。

## windows系统搭建 ##

> 系统环境：windows 10 + python 3.6 + OpenCV 3.4.1


### 一、安装python ###

python的安装之前在[python自学笔记](https://github.com/vipstone/python)的项目中描述了，在这不做重复说明，有需要的朋友，点击查看：[python环境安装](https://github.com/vipstone/python/blob/master/%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.md)

### 二、安装numpy模块 ###

根据上文提示，现在我们已经正确安装了python和pip（安装和管理python包的工具），在正式安装OpenCV之前，首先我们要安装numpy模块。
numpy：是一个定义了数值数组和矩阵类型和它们的基本运算的语言扩展，OpenCV引用了numpy模块，所以安装OpenCV之前必须安装numpy。

本文安装python模块使用的是.whl文件安装的。

**whl文件是什么？**

whl是一个python的压缩包，其中包含了py文件以及经过编译的pyd文件。

**whl安装命令**
> pip3 install 存放路径\xxx.whl

回到主题，我们是要安装numpy模块的。

第一步：先去网站下载对应的numpy版本，下载地址：https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy 本人是64为系统python3.6所以对应的最新版本是：numpy‑1.14.2+mkl‑cp36‑cp36m‑win_amd64.whl，点击下载到D:根目录。

百度云链接：https://pan.baidu.com/s/10RefansrC4_0zsNehjyKTg

提取密码：gua3


第2步：启动命令窗体运行
> pip3 install d:\numpy‑1.14.2+mkl‑cp36‑cp36m‑win_amd64.whl

命令窗体显示：

Processing d:\numpy-1.14.2+mkl-cp36-cp36m-win_amd64.whl

Installing collected packages: numpy

Successfully installed numpy-1.14.2+mkl

说明已经安装成功。


### 三、安装OpenCV ###
同样安装OpenCV模块和numpy方式类似。

第1步：实现去网站下载OpenCV对于的.whl版本压缩包，网址：https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv 本人下载的版本是：opencv_python‑3.4.1‑cp36‑cp36m‑win_amd64.whl 64位系统对应python3.6的，下载到d盘根目录。

百度云链接：https://pan.baidu.com/s/10RefansrC4_0zsNehjyKTg

提取密码：gua3

第2步：启动命令窗体运行
> pip3 install d:\opencv_python-3.4.1-cp36-cp36m-win_amd64.whl

窗体显示：

Processing d:\opencv_python-3.4.1-cp36-cp36m-win_amd64.whl

Installing collected packages: opencv-python

Successfully installed opencv-python-3.4.1

说明安装成功。

### 四、运行OpenCV ###
到此，我们的环境配置已经完成了，终于到了可以撸代码的时刻了，想想还有一点小激动呢。


``` python
import cv2

print(cv2.__version__)

# 输出：3.4.1
```
上面我们简单的打印了OpenCV的版本号，如果能正常输出不报错，说明我们已经把OpenCV的python环境搭建ok了。

什么？感觉还不过瘾，那就来撸一张图，用OpenCV把它展示出来，代码如下：
``` python
import cv2

filepath = "img/meinv.png"
img = cv2.imread(filepath)
cv2.namedWindow('Image')
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

展示效果如图：![正在加载图片](https://raw.githubusercontent.com/vipstone/opencvLab/master/res/show-meinv.png)


----------

下一节：[图片人脸检测（OpenCV版）](detectionOpenCV.md)