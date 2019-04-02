#请使用反向投影技术对局部图片局部特征进行检测和匹配
import cv2
import numpy as np
if __name__ == '__main__':
    #把图像空间从BGR转化为HSV
    img01 = cv2.imread('./img3.jpg')
    h0 = cv2.cvtColor(img01, cv2.COLOR_BGR2HSV)
    img02 = cv2.imread('./img4.jpg')
    h = cv2.cvtColor(img02, cv2.COLOR_BGR2HSV)
    #统计h0的直方图：
    rh = cv2.calcHist([h0], [0, 1], None, [180, 256], [0, 180, 0, 256])
    #归一化直方图的数据：
    cv2.normalize(rh, rh, 0, 255, cv2.NORM_MINMAX)
    #把h0的直方图反向投影到h上面：
    dst = cv2.calcBackProject([h], [0, 1], rh, [0, 180, 0, 256], 1)
    d = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dst = cv2.filter2D(dst, -1, d)
    ret, tr = cv2.threshold(dst, 50, 255, 0)
    tr = cv2.merge((tr, tr, tr))
    res = cv2.bitwise_and(img02, tr)
    s = np.row_stack((img02, tr, res))
    cv2.imshow('img',s)
    cv2.imshow('img02',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()