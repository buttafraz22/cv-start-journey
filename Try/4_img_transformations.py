import cv2 as cv
import numpy as np

img = cv.imread('img/img.png')


def translate(image, x, y):
    """Translates an image along the given x and y in pixels.
    -x for left, -y for up, +x for right, +y for down
    """
    M = np.float32([
        [1, 0, x],
        [0, 1, y]
    ])
    dsize = (image.shape[1], image.shape[0])    # height * width
    return cv.warpAffine(image, M, dsize)


translated = translate(img, 100, 100)
# cv.imshow('Translated image', translated)


def rotate(image, angle, rot_point=None):
    """Rotates an image"""
    height, width = image.shape[:2]
    dsize = (height, width)

    if rot_point is None:
        rot_point = (height//2, width//2)

    M = cv.getRotationMatrix2D(rot_point, angle, scale=1.0)   # we are not interested in scaling the image so 1.0
    return cv.warpAffine(image, M, dsize)


rotated = rotate(img, 45)
# cv.imshow('Rotated image', rotated)

# FLIPPING THE IMAGE
"""0 for vertical, 1 for horizontal, and -1 for both"""
flip_vertical = cv.flip(img, 0)
# cv.imshow('Vertical Flipped', flip_vertical)
flip_horizontal = cv.flip(img, 1)
# cv.imshow('Horizontal Flipped', flip_horizontal)
flip_both = cv.flip(img, -1)
# cv.imshow('Both Flipped', flip_both)

cv.waitKey(0)
