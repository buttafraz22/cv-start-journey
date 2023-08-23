import cv2 as cv

img = cv.imread('img/img.png')
# cv.imshow('Image', img)

# Converting to grayscale
# ----------------------------------------------
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('GrayScale', gray)

# Blur the image. We will use a basic blur, that is Gaussian Blur
# ----------------------------------------------
blur = cv.GaussianBlur(img, (15, 15), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade
# ----------------------------------------------
canny = cv.Canny(img, 125, 125)  # Pass blur here to reduce the edges
# cv.imshow('Canny Edges', canny)

# Dilate an image using the specific structuring elements (the canny edges)
# ----------------------------------------------
dilated = cv.dilate(canny, (7, 7), iterations=3)
# cv.imshow('Dilated', dilated)

# Eroding the dilated image
# ----------------------------------------------
eroded = cv.erode(dilated, (7, 7), iterations=3)
# cv.imshow('Eroded', eroded)

# Resize (cv.RESIZE), ignores the aspect ratio
# ----------------------------------------------
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.INTER_AREA for resize to smaller size. cv.INTER_LINEAR and cv.INTER_CUBIC for low to high resizing.
# INTER_CUBIC is slowest, but results in most high quality image.
# cv.imshow('Resized', resized)

# Cropping the image
# ----------------------------------------------
cropped = img[50:200, 50:200]
# cv.imshow('Cropped', cropped)
cv.waitKey(0)
