#请对比以下两张图相似性，并给出结果数据和所使用的方法参数
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    img1 = cv.imread('./img1.jpg',cv.IMREAD_ANYCOLOR)
    img2 = cv.imread('./img2.jpg',cv.IMREAD_ANYCOLOR)
    histGrayImage1 = cv.calcHist([img1], [1], None, [256], [0, 256])
    cv.normalize(histGrayImage1, histGrayImage1, 0, 255 * 0.9, cv.NORM_MINMAX)
    histGrayImage2 = cv.calcHist([img2], [1], None, [256], [0, 256])
    cv.normalize(histGrayImage2, histGrayImage2, 0, 255 * 0.9, cv.NORM_MINMAX)
    plt.subplot(2, 1, 1)
    plt.plot(histGrayImage1)
    plt.subplot(2, 1, 2)
    plt.plot(histGrayImage2)
    plt.show()

    retval1 = cv.compareHist(histGrayImage1, histGrayImage2, cv.HISTCMP_BHATTACHARYYA)
    print("巴氏距离比较: {}".format(retval1))
    retval2 = cv.compareHist(histGrayImage1, histGrayImage2, cv.HISTCMP_CORREL)
    print("相关性比较: {}".format(retval2))
    retval3 = cv.compareHist(histGrayImage1, histGrayImage2, cv.HISTCMP_CHISQR)
    print("卡方比较: {}".format(retval3))
    cv.waitKey(0)