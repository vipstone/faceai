#coding=utf-8
#图片基础
import cv2
import numpy as np

img = cv2.imread("img/ag.png")

# shape = img.shape  # 形状 (高,宽,3通道[彩色图])
# size = img.size  # 像素总数
# dtype = img.dtype  # uint8 图片类型

# roi = img[200:350, 300:330]  # [y轴选取区域，x轴选取区域]
# img[0:150, 100:130] = roi
# cv2.imshow("image", img)

b, g, r = cv2.split(img)  #分割通道
img = cv2.merge((b, g, r))  #合并通道

img = img[:, :, 0]

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
