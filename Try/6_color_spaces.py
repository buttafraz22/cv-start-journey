# From this code forward, advanced concepts of openCV will be discussed.
# A color space is an array of colors in pixels (RGB is a color space).
import cv2 as cv

img = cv.imread('img/img.png')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('GrayScale', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('Rgb', rgb)

# You can not directly convert grayscale to hsv, lab and vice versa. Any other color
# space conversion code exists in the openCV module itself. For grayscale to LAB or HSV,
# you can first convert it into BGR and then to HSV/LAB.

# !!!!!!    IMPORTANT   !!!!!!
# OpenCV uses BGR format as its default image renderer. If we use another library, say matplotlib,
# code provided in comment below, what would it do is that it would show the image in RGB format (inverting it).
# Keep this in mind. Here is the code below.

# import matplotlib.pyplot as plt
# plt.imshow(img)
# plt.show()
# Notice the difference between img and plt.show()'s image.

cv.waitKey(0)
