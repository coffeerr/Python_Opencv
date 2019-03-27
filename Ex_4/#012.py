import numpy as  np
import cv2
import matplotlib.pyplot as plt
import pytesseract

if __name__ == '__main__':
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    image = cv2.imread('./1.jpg',cv2.COLOR_GRAY2BGR)
    Imax = np.max(image)
    Imin = np.min(image)
    Omin,Omax = 0,255
    a = float(Omax - Omin)/(Imax - Imin)
    b = Omin - a * Imin
    O = a*image + b
    O = O.astype(np.uint8)

    ret,thresh1 = cv2.threshold(O,110,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh1, kernel)
    text = pytesseract.image_to_string(dilated, lang='eng')
    print(text)

    cv2.imshow('img',thresh1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()