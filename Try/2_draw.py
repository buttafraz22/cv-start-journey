import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

# ---------------------------------------
# Step 1 : Paint the image a certain color
# ---------------------------------------
# blank[:] = 0, 255, 0    # this line colors the all image
# blank[200:300, 300:400] = 0, 255, 0  # this line will color certain area over the black square
# cv.imshow('Green', blank)



# ---------------------------------------
# Step 2: Draw a Rectangle over the image
# ---------------------------------------
# cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=cv.FILLED)
# # pt2 is actually ending, we can play around with as per our likings
# # we can set thickness=cv.FILLED to fill the shape with specified color. thickness=-1 also does the same
# # instead of hard coding pt2, we can also put (250,250) for the same result.
#
# cv.imshow('Rectangle', blank)



# ---------------------------------------
# Step 3: Draw a Circle
# ---------------------------------------
# cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 255, 0), thickness=cv.FILLED)
# cv.imshow('Circle', blank)

# ---------------------------------------
# Step4: Draw a line
# ---------------------------------------
# cv.line(blank, (100, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)


# ---------------------------------------
# Write Text on an image
# ---------------------------------------
# cv.putText(blank, 'Hello World', (0, 255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
# cv.imshow('Text', blank)

cv.waitKey(0)
