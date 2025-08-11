import cv2 as cv
import numpy as np

img = cv.imread("Images\\CuteCat.jpg")
#USING KEYWORD
# gray = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error loading the image")        
else:
    #USING LIBRARY
   ''' gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    resized_img = cv.resize(gray, (800,600))
    cv.imshow("Gray", resized_img)
    cv.waitKey(0)
    cv.destroyAllWindows()'''
    

# Using average method
gray = np.mean(img, axis = 2).astype(np.uint8)
resizeimg = cv.resize(gray, (800,600))
cv.imshow("Gray Average", resizeimg)
cv.waitKey(0)
cv.destroyAllWindows()