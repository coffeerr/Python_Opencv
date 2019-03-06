# -*- coding: utf-8 -*-
#实现程序进行基本的图像读取和像素处理
import cv2
import sys
import numpy as np
# 椒盐化图片
def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j,i] = 255
        elif img.ndim == 3:
            img[j,i,0]= 255
            img[j,i,1]= 255
            img[j,i,2]= 255
    return img
if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     image = cv2.imread(sys.argv[1],cv2.IMREAD_ANYCOLOR)
    # else:
    #     print('Usge:python firstOpenCV3.py imageFile')
    image = cv2.imread("./001.jpg",cv2.IMREAD_ANYCOLOR)
    cv2.imshow('image',image)
    image2 = salt(image,500)
    cv2.imshow('image2',image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()