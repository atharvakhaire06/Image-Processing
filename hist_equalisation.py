import cv2 as cv
import numpy as np

# img = cv.imread("Images\\originalfaded.jpg")
img = cv.imread("Images\\girl.webp")

if img is None:
    print("Error Loading in Image")
else: 
    ycrcb = cv.cvtColor(img , cv.COLOR_BGR2YCrCb)  # ycrcb works good for colored images
    y,cr,cb = cv.split(ycrcb)
    y_eq = cv.equalizeHist(y) 

    ycrcb_eq = cv.merge((y_eq, cr,cb))  #merge with other channels

    y_final = cv.cvtColor(ycrcb_eq , cv.COLOR_YCrCb2BGR)
    resized_img = cv.resize(y_final, (600, 400))  
    resizeog = cv.resize(img, (600,400))
    cv.imshow('Original Image',resizeog)
    cv.imshow('Enhanced Image',resized_img)
    cv.waitKey(0)
    cv.destroyAllWindows()