import cv2 as cv

# Lendo e mostrando uma imagem
img = cv.imread('imgs/gato_grande.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)

# Lendo frame por frame de um video e mostrando
capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
