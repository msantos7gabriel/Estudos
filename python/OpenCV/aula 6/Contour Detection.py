import cv2 as cv
import numpy as np

img = cv.imread('imgs/gato.jpg')
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blank = np.zeros(img.shape, dtype='uint8')
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 150, 175)

cv.imshow('Grey', grey)
cv.imshow('Cat2', canny)

ret, thresh = cv.threshold(grey, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contornos, hierarquia = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# RETR_TREE = todos os contornos hierárquicos
# RETR_EXTERNAL = todos os contornos externos
# RETR_LIST = todos os contornos

cv.drawContours(blank, contornos, -1, (0, 0, 255), 1)
cv.imshow('Contornos desenhados', blank)
print(f'{len(contornos)} contornos foram encontrados!')

cv.waitKey(0)
