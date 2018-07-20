# OpenCV Setting up and Introducation #

This tutorial is going to illustrate the installation of Python3.x on both Linux and Windows.
And introduce OpenCV on top of Python.

## OpenCV setting up in Windows ##

> Env：windows 10 + python 3.6 + OpenCV 3.4.1


### 1 Install Python ###

In this [Pthon study note](https://github.com/vipstone/python)I've elaborated the Python install instructions：[Python setup](https://github.com/vipstone/python/blob/master/%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.md)

### 2 Install Python package NumPy ###

After above step, we should have Python and pip (package management system used to install and manage software packages written in Python) installed. Before OpenCV acutal installed we should have Numpy settled, which is a fundamental package for scientific computing with Python, OpenCV depends on Numpy, so it's the prerequisite for OpenCV.

we're using .whl files to install Python packages.

**What is a whl file ?**

whl file are compressed built-package format used for Python.

**Install whl package for Python**
> pip3 install path_to\xxx.whl

Go back the Numpy installation.

Step 1：Download corresponding whl files from here：https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
E.g. Windows 64 with Python 3.6 should download this file: numpy‑1.14.2+mkl‑cp36‑cp36m‑win_amd64.whl

Download from Baidu Yunpan：https://pan.baidu.com/s/10RefansrC4_0zsNehjyKTg

Password：gua3


Step 2：Input Command-line in a terminal
> pip3 install d:\numpy‑1.14.2+mkl‑cp36‑cp36m‑win_amd64.whl

Output：

Processing d:\numpy-1.14.2+mkl-cp36-cp36m-win_amd64.whl

Installing collected packages: numpy

Successfully installed numpy-1.14.2+mkl


### 3 Install OpenCV as Python package ###
Similar way to install OpenCV.

Step 1：Download corresponding whl files from here：https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv E.g Windows 64 with Python 3.6 should download this file:：opencv_python‑3.4.1‑cp36‑cp36m‑win_amd64.whl

Download from Baidu Yunpan：https://pan.baidu.com/s/10RefansrC4_0zsNehjyKTg

Password：gua3

Step 2：Input Command-line in a terminal
> pip3 install d:\opencv_python-3.4.1-cp36-cp36m-win_amd64.whl

Output：

Processing d:\opencv_python-3.4.1-cp36-cp36m-win_amd64.whl

Installing collected packages: opencv-python

Successfully installed opencv-python-3.4.1


### 4 OpenCV examples ###

``` python
import cv2

print(cv2.__version__)

# Output：3.4.1
```
If the version number can be print out correctly which means OpenCV-Python is settled.

Show an image with OpenCV：
``` python
import cv2

filepath = "img/meinv.png"
img = cv2.imread(filepath)
cv2.namedWindow('Image')
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

----------
## OpenCV setting up in Linux ##

>Ubuntu 18.04
>Python 3.6.5
>Pip 10.0.1
>Numpy 1.14.3
>OpenCV 3.4.0

Ubuntu already had Python built in which is easier for setting campare to Windows, so just using apt-get command in Ubuntu for software package installation. Please refer this [tutorial](http://www.cnblogs.com/vipstone/p/9038023.html) for software sources updating (if needed).

### Installation ###

It's easier in Ubuntu than Windows for OpenCV installation, basically we only need pip command to do all the work.

#### Install Numpy ####
CLI：pip3 install numpy

Try below Python code to see if Numpy settled
```
import numpy 

numpy.__version__
```
If version number print out correctly which means Numpy installed successfully.

#### Install OpenCV ####
Similar way to install OpenCV:
>pip3 install opencv-python

Try below Python code to see if OpenCV settled
```
import cv2 

cv2.__version__
```
If version number print out correctly which means OpemCV installed successfully.

# FAQ #

[1] python3: Relink `/lib/x86_64-linux-gnu/libudev.so.1` with `/lib/x86_64-linux-gnu/librt.so.1` for IFUNC symbol `clock_gettime`
Segmentation fault (core dumped)

Answer：apt install python3-opencv


----------

