# A color channel is a stream of colors (Red, Green, Blue) etc. OpenCV allows us to split an image into multiple
# color channels.
import cv2 as cv

img = cv.imread('img/img.png')
cv.imshow('Original', img)

b, g, r = cv.split(img)
# cv.imshow('Blue', b)
# cv.imshow('Red', r)
# cv.imshow('Green', g)
merged = cv.merge([b, g, r])
# cv.imshow('merged', merged)

# Let's merge a blue image over a blank one.
import numpy as np
blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b, blank, blank])
# cv.imshow('Blue', blue)
green = cv.merge([blank, g, blank])
# merge the correct color in its correct place. So Green occurs second in BGR.
# blue first,  red third
red = cv.merge([blank, blank, r])
# cv.imshow('Red', red)

# comp = cv.merge([blue, green, red])
# this above line will throw an error. because for each component, there are three channels.
# so total 9 channels, which will throw an error.
cv.waitKey(0)
