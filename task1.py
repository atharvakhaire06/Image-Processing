import cv2 as cv
import numpy as np

img = cv.imread("Images\\CuteCat.jpg")
if img is None:
    print("Error loading the image")
else:
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    resized_img = cv.resize(gray, (800,600))
    cv.imshow("Gray", resized_img)
    cv.waitKey(0)
    cv.destroyAllWindows()