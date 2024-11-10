import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30),
                         (370, 370), 255, thickness=cv.FILLED)

circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('RET', rectangle)
cv.imshow('Cir', circle)

#  Mostra as regiões de intercessão
bitwise_and = cv.bitwise_and(circle, rectangle)
cv.imshow('and', bitwise_and)

#  Mostra as regiões de intercessão e as de não intercessão
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('or', bitwise_or)

#  Mostra as de não intercessão
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('xor', bitwise_xor)

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('not', bitwise_not)


cv.waitKey(0)
