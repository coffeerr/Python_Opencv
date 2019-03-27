#画出灰度直方图
import numpy as  np
import cv2
import matplotlib.pyplot as plt


if __name__ == '__main__':
    image = cv2.imread('./1.jpg',0)
    hist = cv2.calcHist([image],[0],None,[256],[0,256])
    plt.hist(image.ravel(),256,[0,256])
    plt.show()
