import cv2
import numpy as np
from scipy import ndimage
core = 11
if __name__ == '__main__':
    img = cv2.imread('./#014_2.jpg',0)
    blurResult = cv2.blur(img, (core, core))
    gaussianResult = cv2.GaussianBlur(img, (core, core), 1.5)
    medianBlurResult = cv2.medianBlur(img, core)
    cv2.imshow('medianBlurResult',medianBlurResult)
    cv2.imshow('gaussianResult',gaussianResult)
    cv2.imshow('blurResult',blurResult)
    cv2.waitKey(0)
    cv2.destroyAllWindows()