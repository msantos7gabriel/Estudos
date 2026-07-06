import cv2 as cv

img = cv.imread('imgs/gato.jpg')
# cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Img Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Img Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 1)
cv.imshow('Adaptive Thresh', adaptive_thresh)

cv.waitKey(0)
