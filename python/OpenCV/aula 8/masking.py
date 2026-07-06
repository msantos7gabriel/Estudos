import cv2 as cv
import numpy as np


img = cv.imread('imgs/gato.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(
    blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 200, 255, thickness=-1)
# cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

cv.waitKey(0)
