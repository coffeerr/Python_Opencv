#请使用numpy的 concatenate对两张大小一样的图像进行横向拼接
import cv2
import numpy


if __name__ ==  '__main__':
    image1 = cv2.imread('./image1.jpg',cv2.IMREAD_ANYCOLOR)
    image2 = cv2.imread('./image2.jpg', cv2.IMREAD_ANYCOLOR)
    image3 = numpy.concatenate((image1,image2),axis=1)
    cv2.imshow('image',image3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()