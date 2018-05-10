#coding=utf-8
#直方图

import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签

# ut = np.zeros(256, dtype=img.dtype)  #创建空的查找表
# hist = cv2.calcHist(
#     [img],  #计算图像的直方图
#     [0],  #使用的通道
#     None,  #没有使用mask
#     [256],  #it is a 1D histogram
#     [0.0, 255.0])

# def calcAndDrawHist(image, color):
#     hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
#     minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
#     histImg = np.zeros([256, 256, 3], np.uint8)
#     hpt = int(0.9 * 256)

#     for h in range(256):
#         intensity = int(hist[h] * hpt / maxVal)
#         cv2.line(histImg, (h, 256), (h, 256 - intensity), color)

#     return histImg

# img = cv2.imread("img/hist.png")
# b, g, r = cv2.split(img)

# print(b)
# print(g)
# print(r)

# histImgB = calcAndDrawHist(b, [255, 0, 0])
# histImgG = calcAndDrawHist(g, [0, 255, 0])
# histImgR = calcAndDrawHist(r, [0, 0, 255])

# cv2.imshow("histImgB", histImgB)
# cv2.imshow("histImgG", histImgG)
# cv2.imshow("histImgR", histImgR)

# #灰色直方图均衡化
# img = cv2.imread("img/hist.png", 0)
# equ = cv2.equalizeHist(img)
# cv2.imshow("old image", img)

# cv2.imshow("image", equ)

##彩色直方图均衡化
# img = cv2.imread("img/hist.png")
# ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
# channels = cv2.split(ycrcb)
# cv2.equalizeHist(channels[0], channels[0])  #输入通道、输出通道矩阵
# cv2.merge(channels, ycrcb)  #合并结果通道
# cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)
# cv2.imshow("old image", cv2.imread("img/hist.png"))
# cv2.imshow("image", img)

##绘制直方图
# img = cv2.imread("img/hist.png")
# chans = cv2.split(img)
# colors = ("b", "g", "r")
# plt.figure()
# plt.title("直方图分布")
# plt.xlabel("颜色值")
# plt.ylabel("像素点")
# for (chan, color) in zip(chans, colors):
#     hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
#     plt.plot(hist, color=color)
#     plt.xlim([0, 256])
# plt.show()

# #添加噪声
# img = cv2.imread("img/black.png")

# for k in range(0, 1000):
#     xi = int(np.random.uniform(0, img.shape[1]))
#     xj = int(np.random.uniform(0, img.shape[0]))
#     if img.ndim == 2:
#         img[xj, xi] = 255
#     elif img.ndim == 3:
#         img[xj, xi, 0] = 255
#         img[xj, xi, 1] = 255
#         img[xj, xi, 2] = 255
# cv2.imwrite("img/black-noise.png", img)
# cv2.imshow("image", img)

# #滤波器
img = cv2.imread("img/black-noise.png")

dst = cv2.blur(img, (5, 5))  #均值滤波
gaussian = cv2.GaussianBlur(img, (5, 5), 1)  #高斯滤波
median = cv2.medianBlur(img, 5)  #中值滤波
cv2.imshow("image", gaussian)

# #Sobel算子 —— 是一种带有方向性的滤波器
# img = cv2.imread('img/ag.png', cv2.IMREAD_COLOR)
# x = cv2.Sobel(
#     img, cv2.CV_16S, 1, 0
# )  #cv2.CV_16S -- Sobel 函数求完导数后会有负值和大于255的值，而原图像是uint8（8位无符号数据），所以在建立图像时长度不够，会被截断，所以使用16位有符号数据
# y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
# absx = cv2.convertScaleAbs(
#     x)  #convertScaleAbs() --  转回uint8形式，否则将无法显示图像，而只是一副灰色图像
# absy = cv2.convertScaleAbs(y)
# dist = cv2.addWeighted(absx, 0.5, absy, 0.5, 0)  #参数2：第1张图的权重；参数4：第2张图的权重
# # cv2.imshow('y', absy)
# # cv2.imshow('x', absx)
# cv2.imshow('dsit', dist)
# cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()