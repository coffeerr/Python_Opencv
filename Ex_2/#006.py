#006 通过图像矩阵对图像进行上下翻转
import cv2
import numpy as np
if __name__ == '__main__':
    img = cv2.imread('./004.jpg',cv2.IMREAD_ANYCOLOR)
    cv2.imshow('img1',img)
    rImg = cv2.rotate(img,cv2.ROTATE_180)
    cv2.imshow('img2',rImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()