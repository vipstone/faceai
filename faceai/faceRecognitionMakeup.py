#coding=utf-8
#数字化妆类
import face_recognition
from PIL import Image, ImageDraw

#加载图片到numpy array
image = face_recognition.load_image_file("img/ag.png")

#标识脸部特征
face_landmarks_list = face_recognition.face_landmarks(image)

for face_landmarks in face_landmarks_list:
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image, 'RGBA')

    # 绘制眉毛
    d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
    d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

    # 绘制嘴唇
    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    # 绘制眼睛
    d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
    d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

    # 绘制眼线
    d.line(
        face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]],
        fill=(0, 0, 0, 110),
        width=6)
    d.line(
        face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]],
        fill=(0, 0, 0, 110),
        width=6)

    pil_image.show()