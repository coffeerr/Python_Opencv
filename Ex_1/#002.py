# -*- coding: utf-8 -*-
#通过像素操作，将图片任一颜色通道设置为0并输出图片
import cv2
import numpy as np
if __name__ == '__main__':
    image = cv2.imread("./001.jpg",cv2.IMREAD_ANYCOLOR)
    cv2.imshow('image1',image)
    b = image[:, :, 0]
    g = image[:, :, 1]
    r = image[:, :, 2]
    image2 = cv2.merge([r,g,b*0])
    cv2.imshow('image2', image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
