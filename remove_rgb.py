import cv2 as cv
import numpy as np
# [:, :, 0] = Red 


img = cv.imread("Images\\images.jpeg")
if img is None:
    print("Error loading the image")
else:
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # img[:, :, 0] = 0 #Red

    rgb[:, :, 1] = 0  #Green
    rgb = cv.cvtColor(img, cv.COLOR_RGB2BGR)

    # img[:, :, 2] = 0 Blue

    resized_img = cv.resize(rgb, (500,400))
    cv.imshow('RGB PLANES',resized_img)
    cv.waitKey(0)
    cv.destroyAllWindows()