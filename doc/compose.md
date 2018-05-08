# 头像特效合成

实现思路：使用OpenCV检测出头部位置，向上移动20像素添加虚拟帽子，帽子的宽度等于脸的大小，高度等比缩小，需要注意的是如果高度小于脸部向上移动20像素的值，那么帽子的高度就等于最小高度=（脸部位置-20）。
为什么是20而不是30或者40，因为取得是检测的脸部和头顶的一般距离20，开发者可自己调整。


**注意事项**

图片合成元件，要是黑背景图片，透明的图片也会有问题，在ps手动处理一下透明图片，添加新图层，选中alt+Del添加黑背景，把新图层层级放到最底部即可。

# 效果图预览 #
<img src="https://raw.githubusercontent.com/vipstone/faceai/master/res/compose.png" width = "200" height = "300" alt="头像特效合成"  />


## 代码实现 ##
```
#coding=utf-8
import cv2

# OpenCV人脸识别分类器
classifier = cv2.CascadeClassifier(
    "C:\Python36\Lib\site-packages\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml"
)

img = cv2.imread("img/ag-3.png")  # 读取图片
imgCompose = cv2.imread("img/compose/maozi-1.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换灰色
color = (0, 255, 0)  # 定义绘制颜色
# 调用识别人脸
faceRects = classifier.detectMultiScale(
    gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
if len(faceRects):  # 大于0则检测到人脸
    for faceRect in faceRects:  
        x, y, w, h = faceRect
        sp = imgCompose.shape
        imgComposeSizeH = int(sp[0]/sp[1]*w)
        if imgComposeSizeH>(y-20):
            imgComposeSizeH=(y-20)
        imgComposeSize = cv2.resize(imgCompose,(w, imgComposeSizeH), interpolation=cv2.INTER_NEAREST)
        top = (y-imgComposeSizeH-20)
        if top<=0:
            top=0
        rows, cols, channels = imgComposeSize.shape
        roi = img[top:top+rows,x:x+cols]

        # Now create a mask of logo and create its inverse mask also
        img2gray = cv2.cvtColor(imgComposeSize, cv2.COLOR_RGB2GRAY)
        ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY) 
        mask_inv = cv2.bitwise_not(mask)

        # Now black-out the area of logo in ROI
        img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

        # Take only region of logo from logo image.
        img2_fg = cv2.bitwise_and(imgComposeSize, imgComposeSize, mask=mask)

        # Put logo in ROI and modify the main image
        dst = cv2.add(img1_bg, img2_fg)
        img[top:top+rows, x:x+cols] = dst

cv2.imshow("image", img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
```

