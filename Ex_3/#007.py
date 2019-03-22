#007  请通过opencv几何变换对图像进行旋转45度和放大两倍，但保留原始图片不被裁剪，从而得到新的图片
import cv2
import numpy


if __name__ == '__main__':
    img = cv2.imread('./image1.jpg',cv2.IMREAD_ANYCOLOR)
    h,w = img.shape[:2]
    #旋转45度
    A = cv2.getRotationMatrix2D((w/2.0,h/2.0),45,0.5)
    img2 = cv2.warpAffine(img,A,(w,h),borderValue=125)
    cv2.imshow('img2',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

