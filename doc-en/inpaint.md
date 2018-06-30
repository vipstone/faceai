# 图片修复程序-可用于水印去除 #

在现实的生活中，我们可能会遇到一些美好的或是珍贵的图片被噪声干扰，比如旧照片的折痕，比如镜头上的灰尘或污渍，更或者是某些我们想为我所用但有讨厌水印，那么有没有一种办法可以消除这些噪声呢？

答案是肯定的，依然是被我们用了无数次的OpenCV这款优秀的框架。

# 效果预览 #
![](http://icdn.apigo.cn/inpaint.png?1)

# 图片修复原理 #
那OpenCV究竟是怎么实现的，简单的来说就是开发者标定噪声的特征，在使用噪声周围的颜色特征推理出应该修复的图片的颜色，从而实现图片修复的。

# 程序实现解析 #
1. 标定噪声的特征，使用cv2.inRange二值化标识噪声对图片进行二值化处理，具体代码：cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))，把[240, 240, 240]~[255, 255, 255]以外的颜色处理为0；
1. 使用OpenCV的dilate方法，扩展特征的区域，优化图片处理效果；
2. 使用inpaint方法，把噪声的mask作为参数，推理并修复图片；

# 完整代码 #
```
#coding=utf-8
#图片修复

import cv2
import numpy as np

path = "img/inpaint.png"

img = cv2.imread(path)
hight, width, depth = img.shape[0:3]

#图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))

#创建形状和尺寸的结构元素
kernel = np.ones((3, 3), np.uint8)

#扩张待修复区域
hi_mask = cv2.dilate(thresh, kernel, iterations=1)
specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)

cv2.namedWindow("Image", 0)
cv2.resizeWindow("Image", int(width / 2), int(hight / 2))
cv2.imshow("Image", img)

cv2.namedWindow("newImage", 0)
cv2.resizeWindow("newImage", int(width / 2), int(hight / 2))
cv2.imshow("newImage", specular)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

图片扩展与腐蚀更多资料：[http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html)
