## 004请通过numpy或Mat来实现对像素矩阵的操作，读入一张图片并打印像素矩阵数字
import cv2
import numpy as np

if __name__ == '__main__':
    image = cv2.imread('./004.jpg',cv2.IMREAD_ANYCOLOR)
    img_arr = np.array(image)
    print(img_arr)
    cv2.imshow('004',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
