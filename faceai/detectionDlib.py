#coding=utf-8
#图片检测 - Dlib版本
import cv2
import dlib

path = "img/ag.png"
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#人脸分类器
detector = dlib.get_frontal_face_detector()
# 获取人脸检测器
predictor = dlib.shape_predictor(
    "C:\\Python36\\Lib\\site-packages\\dlib-data\\shape_predictor_68_face_landmarks.dat"
)

dets = detector(gray, 1)
for face in dets:
    # 在图片中标注人脸，并显示
    # left = face.left()
    # top = face.top()
    # right = face.right()
    # bottom = face.bottom()
    # cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
    # cv2.imshow("image", img)

    shape = predictor(img, face)  # 寻找人脸的68个标定点
    # 遍历所有点，打印出其坐标，并圈出来
    for pt in shape.parts():
        pt_pos = (pt.x, pt.y)
        cv2.circle(img, pt_pos, 1, (0, 255, 0), 2)
    cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()