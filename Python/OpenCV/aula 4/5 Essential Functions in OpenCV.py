import cv2 as cv

img = cv.imread('imgs/gato.jpg')
# cv.imshow('Normal', img)

# Convertendo para grayscale
cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('cinza', cinza)

# Blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

# Dilating the img
dilated = cv.dilate(canny, (7, 7), iterations=3)
# cv.imshow('dilate', dilated)

# Eroding
eroded = cv.erode(dilated, (5, 5), iterations=2)
# cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (700, 700), interpolation=cv.INTER_LINEAR)
resized_2 = cv.resize(img, (700, 700), interpolation=cv.INTER_CUBIC)
# INTER_AREA = Usado para quando se deseja redimensionar o tamanho da imagem para um menor que a imagem padrão
# INTER_LINEAR = Usado para quando se deseja redimensionar o tamanho da imagem para um maior que a imagem padrão
# INTER_CUBIC = Usado para quando se deseja redimensionar o tamanho da imagem para um maior que a imagem padrão porem é o mais lento e de maior qualidade da imagem
# cv.imshow('Resized_linear', resized)
# cv.imshow('Resized_cubic', resized_2)

# Cropping
cropped = img[0:350, 90:375]
cv.imshow('Croped', cropped)

cv.waitKey(0)
