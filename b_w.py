import cv2 as cv
import numpy as np
img = cv.imread("Images\\CuteCat.jpg")
if img is None:
    print("Error loading the image")
else:
    gray = np.mean(img,axis=2).astype(np.uint8)
    resizeimg = cv.resize(gray,(800,600))
    _,bw = cv.threshold(resizeimg, 127,255,cv.THRESH_BINARY)
    cv.imshow('B&W using average',bw)
    cv.waitKey(0)
    cv.destroyAllWindows()