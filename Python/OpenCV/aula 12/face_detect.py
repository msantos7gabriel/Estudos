import cv2 as cv

img = cv.imread('imgs/group 1.jpg')
# cv.imshow('Pessoa', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Pessoa Cinza', gray)

haar_cascade = cv.CascadeClassifier('aula 12\\haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, minNeighbors=1)

print(f'Numero de faces encontradas é igual a {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=2)
cv.imshow('Faces detectadas', img)

cv.waitKey(0)
