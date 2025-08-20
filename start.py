import cv2 as cv
img = cv.imread("Images\\CuteCat.jpg")
def rescale(frame, scale = 0.8):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
if img is None:
    print("Error Loading in Image")
else:
    # resized_img = cv.resize(img, (800, 600))  direct function
    
    resized_img = rescale(img , scale = 0.1)
    cv.imshow('Cat',resized_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    