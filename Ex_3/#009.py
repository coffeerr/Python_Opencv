#请使用numpy的 concatenate对两张大小一样的图像进行横向拼接
import cv2
import numpy as np
if __name__ ==  '__main__':
    img = cv2.imread('./image1.jpg',cv2.IMREAD_ANYCOLOR)
    h, w = img.shape[:2]
    for xi in range(0,w):
        for xj in range(0,h):
            b = pow((h/2 + w/2),2)
            a = 0.2 * (1 - ((xi - w/2)**2 + (xj - h/2)**2)/(w**2/4 + h**2/4))
            img[xj,xi,0]=int(img[xj,xi,0]*a)
            img[xj,xi,1]=int(img[xj,xi,1]*a)
            img[xj,xi,2]=int(img[xj,xi,2]*a)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()