import cv2 as cv
import numpy as np

img = cv.imread('imgs/gato.jpg')

# Translation


def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dim = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dim)

# -x --> Desloca para Esquerda
# -y --> Desloca para Cima
# x --> Desloca para Direita
# y --> Desloca para Baixo


translated = translate(img, -100, -200)
cv.imshow('Gato Deslocado', translated)

# Rotation


def rotate(img, angle, rotation_point=None):
    (height, width) = img.shape[:2]
    if rotation_point == None:
        rotation_point = (width//2, height//2)
    rot_mat = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dim = (width, height)
    return cv.warpAffine(img, rot_mat, dim)


rotated = rotate(img, -45)
cv.imshow('Gato Rodado', rotated)

# Flipping
flip = cv.flip(img, 1)
# 0 = Gira verticalmente (eixo y)
# 1 = Gira Horizontalmente (eixo x)
# -1 = Gira o eixo x e y 
cv.imshow('Gato Flipado', flip)
cv.waitKey(0)
