#coding=utf-8
#图片检测 - OpenCV版本
import cv2
import numpy as np

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

cv2.imshow("image", img)  # 显示图像
cv2.waitKey(0)
cv2.destroyAllWindows()




