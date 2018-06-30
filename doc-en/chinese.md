# OpenCV添加中文 #
OpenCV添加文字的方法putText(...)，添加英文是没有问题的，但如果你要添加中文就会出现“？？？”的乱码，需要特殊处理一下。

下文提供封装好的（代码）方法，供OpenCV添加中文使用。

# 效果预览 #

<img src="https://raw.githubusercontent.com/vipstone/faceai/master/res/chinese.png" width = "300" height = "200" alt="效果展示"  />

# 实现思路 #
使用PIL的图片绘制添加中文，可以指定字体文件，那么也就是说使用PIL可以实现中文的输出。

有思路之后，接下来的工作就简单了。

1. OpenCV图片格式转换成PIL的图片格式；
1. 使用PIL绘制文字；
1. PIL图片格式转换成OpenCV的图片格式；

# 代码分解 #

**OpenCV图片转换为PIL图片格式**

```
img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
```

**使用PIL绘制文字**
```
draw = ImageDraw.Draw(img)
fontText = ImageFont.truetype("font/simsun.ttc", textSize, encoding="utf-8")
draw.text((left, top), "文字内容", textColor, font=fontText)
```
字体文件为：simsun.ttc，Windows可以在C:\Windows\Fonts下面查找。



**PIL图片格式转换成OpenCV的图片格式**
```
cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)
```


# 完整代码 #

封装好的完整方法

```
#coding=utf-8
#中文乱码处理

import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, numpy.ndarray)):  #判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype(
        "font/simsun.ttc", textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)

```

代码调用

```
img = cv2ImgAddText(img, "大家好，我是星爷", 140, 60, (255, 255, 0), 20)
```