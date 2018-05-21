# 视频对象提取 #



```
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #在PS里用取色器的HSV
    psHSV = [112, 89, 52]
    diff = 40  #上下浮动值
    #因为PS的HSV（HSB）取值是：0~360、0~1、0~1，而OpenCV的HSV是：0~180、0~255、0~255，所以要对ps的hsv进行处理，H/2、SV*255
    lowerHSV = [(psHSV[0] - diff) / 2, (psHSV[1] - diff) * 255 / 100,
                (psHSV[2] - diff) * 255 / 100]
    upperHSV = [(psHSV[0] + diff) / 2, (psHSV[1] + diff) * 255 / 100,
                (psHSV[2] + diff) * 255 / 100]

    mask = cv2.inRange(hsv, np.array(lowerHSV), np.array(upperHSV))

    res = cv2.bitwise_and(frame, frame, mask=mask)
    res = cv2.GaussianBlur(res, (5, 5), 1)

    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
```