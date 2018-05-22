#coding=utf-8
#图片着色
import keras
# import tensorflow as tf
from skimage.io import imread, imsave
from skimage.color import rgb2gray, gray2rgb, rgb2lab, lab2rgb
from keras.models import Sequential
from keras.layers import Conv2D, UpSampling2D, InputLayer, Conv2DTranspose
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
import os
import cv2


def get_train_data(img_file):
    image = img_to_array(load_img(img_file))
    image_shape = image.shape
    image = np.array(image, dtype=float)
    x = rgb2lab(1.0 / 255 * image)[:, :, 0]
    y = rgb2lab(1.0 / 255 * image)[:, :, 1:]
    y /= 128
    x = x.reshape(1, image_shape[0], image_shape[1], 1)
    y = y.reshape(1, image_shape[0], image_shape[1], 2)
    return x, y, image_shape


def build_model():
    model = Sequential()
    model.add(InputLayer(input_shape=(None, None, 1)))
    model.add(Conv2D(8, (3, 3), activation='relu', padding='same', strides=2))
    model.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(16, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(16, (3, 3), activation='relu', padding='same', strides=2))
    model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(32, (3, 3), activation='relu', padding='same', strides=2))
    model.add(UpSampling2D((2, 2)))
    model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
    model.add(UpSampling2D((2, 2)))
    model.add(Conv2D(16, (3, 3), activation='relu', padding='same'))
    model.add(UpSampling2D((2, 2)))
    model.add(Conv2D(2, (3, 3), activation='tanh', padding='same'))
    # model.compile(optimizer='rmsprop', loss='mse')
    model.compile(optimizer='adam', loss='mse')
    return model


#训练数据
def train():
    x, y, img_shape = get_train_data('./img/colorize/colorize-original.png')

    # x2, y2, img_shape2 = get_train_data(
    #     './img/colorize/colorize2-original.png')

    model = build_model()
    num_epochs = 1000  #训练次数
    batch_size = 1

    model.fit(x, y, batch_size=batch_size, epochs=num_epochs)
    # model.fit(x2, y2, batch_size=batch_size, epochs=num_epochs)
    model.save('./data/simple_colorize.h5')


#着色
def colorize():
    path = './img/colorize/colorize2.png'
    # cv2.imwrite('./img/colorize3.png', cv2.imread(path, 0))
    x, y, image_shape = get_train_data(path)
    model = build_model()
    model.load_weights('./data/simple_colorize.h5')
    output = model.predict(x)
    output *= 128
    tmp = np.zeros((200, 200, 3))
    tmp[:, :, 0] = x[0][:, :, 0]
    tmp[:, :, 1:] = output[0]
    colorizePath = path.replace(".png", "-res.png")
    imsave(colorizePath, lab2rgb(tmp))
    cv2.imshow("I", cv2.imread(path))
    cv2.imshow("II", cv2.imread(colorizePath))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # imsave("test_image_gray.png", rgb2gray(lab2rgb(tmp)))


if __name__ == '__main__':
    # train()
    colorize()