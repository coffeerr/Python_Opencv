# coding: utf-8

import numpy as np
import cv2
import random
from matplotlib import pyplot as plt

def add_salt_noise(img, SNR):
    img_ = img.copy()
    c, h, w = img_.shape
    mask = np.random.choice((0, 1, 2), size=(1, h, w), p=[SNR, (1 - SNR) / 2., (1 - SNR) / 2.])
    mask = np.repeat(mask, c, axis=0)     # 按channel 复制到 与img具有相同的shape
    img_[mask == 1] = 255    # 盐噪声
    img_[mask == 2] = 0      # 椒噪声
    return img_


def add_gasuss_noise(image, mean=0, var=0.001):
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    return out
if __name__ == '__main__':
    img = cv2.imread('./img1.jpg')
    SNR_list = [0.9, 0.7, 0.5, 0.3]
    sub_plot = [221, 222, 223, 224]

    img_s = add_salt_noise(img.transpose(2, 1, 0), 0.9)     # c,
    img_s = img_s.transpose(2, 1, 0)
    img_g = add_gasuss_noise(img)
    cv2.imshow('Gaussian',img_g)

    cv2.imshow('Salt', img_s)
    cv2.waitKey(0)
    cv2.destroyAllWindows()