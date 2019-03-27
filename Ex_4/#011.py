import numpy as  np
import cv2
import matplotlib.pyplot as plt


if __name__ == '__main__':
    image = cv2.imread('./1.jpg',cv2.IMREAD_ANYCOLOR)
    Imax = np.max(image)
    Imin = np.min(image)
    Omin,Omax = 0,255
    a = float(Omax - Omin)/(Imax - Imin)
    b = Omin - a * Imin
    O = a*image + b
    O = O.astype(np.uint8)
    cv2.imshow('O',O)
    cv2.waitKey(0)
    cv2.destroyAllWindows()