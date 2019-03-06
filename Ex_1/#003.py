# -*- coding: utf-8 -*-
#实现以下透明叠加图谱效果
import cv2
import numpy as np
def addImage(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img = cv2.imread(img2_path)
    h, w, _ = img1.shape
    # 函数要求两张图必须是同一个size
    img2 = cv2.resize(img, (w,h), interpolation=cv2.INTER_AREA)
    #print img1.shape, img2.shape
    #alpha，beta，gamma可调
    alpha = 0.7
    beta = 1-alpha
    gamma = 0
    img_add = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    # cv2.namedWindow('addImage')
    cv2.imshow('img_add',img_add)
    cv2.waitKey()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    addImage('./002.jpg','./003.jpg')