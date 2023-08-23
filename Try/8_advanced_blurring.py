import cv2 as cv

img = cv.imread('img/img.png')
cv.imshow('Original', img)

# first method : averaging
avg = cv.blur(img, (3, 3))
cv.imshow('Average Blur', avg)

gauss = cv.GaussianBlur(img, (3, 3), 0) #sigmaX is the STDEV in x direction
cv.imshow('Gaussian Blur', gauss)

med = cv.medianBlur(img, 3)
cv.imshow('Median Blur', med)

# bilateral blur keeps the edges, but blurs the pixels themselves. Useful for noise reduction.
bil = cv.bilateralFilter(img, 10, 70, 15)
cv.imshow('Bilateral Blur', bil)
cv.waitKey(0)
