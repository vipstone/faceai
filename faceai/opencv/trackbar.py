#coding=utf-8
#调色板
import cv2
import numpy as np

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')


def callback(x):
    pass


#参数1：名称；参数2：作用窗口，参数3、4：最小值和最大值；参数5：值更改回调方法
cv2.createTrackbar('R', 'image', 0, 255, callback)
cv2.createTrackbar('G', 'image', 0, 255, callback)
cv2.createTrackbar('B', 'image', 0, 255, callback)

while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')

    img[:] = [b, g, r]

cv2.destroyAllWindows()