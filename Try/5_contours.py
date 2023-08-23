import cv2 as cv
import numpy as np

img = cv.imread('img/img.png')
blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 125, 125)
# cv.imshow('Canny', canny)

ret, thres = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
contours, hierarchies = cv.findContours(thres, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'Length of contours is {len(contours)}')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours', blank)

cv.waitKey(0)
