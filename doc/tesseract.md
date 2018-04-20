# Tesseract Ocr

运行环境：
>windows10 + python 3.6 + tesseract 4.0.0-beta.1

先看效果：
![](https://raw.githubusercontent.com/vipstone/faceai/master/res/tesseractOcr.png)

一、安装python模块
>pip3 install pytesseract

二、安装tesseract orc
下载地址：https://github.com/UB-Mannheim/tesseract/wiki 点击“tesseract-ocr-w64-setup-v4.0.0-beta.1.20180414.exe”下载安装。

注意：安装的时候选中中文包。

本人安装目录：C:\Users\Administrator\AppData\Local\Tesseract-OCR

使用命令，查看版本号和支持语言：

>cd C:\Users\Administrator\AppData\Local\Tesseract-OCR
>tesseract -v
>tesseract --list-langs　　#查看Tesseract-OCR支持语言

三、配置tesseract运行文件

C:\Python36\Lib\site-packages\pytesseract\pytesseract.py
找到文件：
>tesseract_cmd = 'tesseract'

修改为：
>tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

四、代码识别

```
from PIL import Image
import pytesseract
import cv2

path = "img\\text-img.png"

text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
print(text)

img = cv2.imread(path)
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
```