#coding=utf-8
#鼠标绘图

import cv2
import numpy as np

# **************** 1 ****************
# for i in dir(cv2):
#     if 'EVENT' in i:
#         print(i)
'''
EVENT_FLAG_ALTKEY  #按住alt键
EVENT_FLAG_CTRLKEY #按住ctrl键
EVENT_FLAG_LBUTTON #按住鼠标左键
EVENT_FLAG_MBUTTON #按住右键点击左键
EVENT_FLAG_RBUTTON #按住鼠标右键
EVENT_FLAG_SHIFTKEY #按住shift键
EVENT_LBUTTONDBLCLK #左键双击
EVENT_LBUTTONDOWN #左键按下
EVENT_LBUTTONUP #左键抬起
EVENT_MBUTTONDBLCLK #滚轮双击
EVENT_MBUTTONDOWN #滚轮按下
EVENT_MBUTTONUP #滚轮抬起
EVENT_MOUSEMOVE #鼠标移动
EVENT_MOUSEWHEEL #鼠标滚轮滚动
EVENT_RBUTTONDBLCLK #右键双击  
EVENT_RBUTTONDOWN #右键按下
EVENT_RBUTTONUP #右键抬起
'''

# # **************** 2 ****************
# def draw_circle(event, x, y, flags, param):
#     if event == cv2.EVENT_MBUTTONDOWN:
#         cv2.circle(img, (x, y), 20, (255, 0, 0), -1)

# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle)

# while (1):
#     cv2.imshow('image', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# **************** 3 happy的自由绘图 ****************
drawing = False


def drawDef(event, x, y, flags, param):
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False

    if event == cv2.EVENT_MOUSEMOVE and drawing == True:
        cv2.circle(img, (x, y), 10, (255, 0, 0), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', drawDef)

while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
