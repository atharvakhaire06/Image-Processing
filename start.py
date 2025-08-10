import cv2 as cv
img = cv.imread("Images\\CuteCat.jpg")
if img is None:
    print("Error Loading in Image")
else:
    resized_img = cv.resize(img, (800, 600))
    cv.imshow('Cat',resized_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
