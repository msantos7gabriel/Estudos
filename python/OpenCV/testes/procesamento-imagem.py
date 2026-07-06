import cv2 as cv

img = cv.imread('../imgs/gato.jpg')
cv.imshow('Imagem sem processamento', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Preto e Branca', gray)

equalized = cv.equalizeHist(gray)
cv.imshow('Equalizando o histograma', equalized)

edges = cv.Canny(equalized, 50, 170)
cv.imshow('Desenho das bordas', edges)

dilated = cv.dilate(edges, (5, 5), iterations=1)
cv.imshow('Dilatando as bordas', dilated)

cv.waitKey(0)
