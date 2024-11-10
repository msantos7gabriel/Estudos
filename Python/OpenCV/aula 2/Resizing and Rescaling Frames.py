import cv2 as cv


def resize(frame, scale=1):
    # Funciona para videos, imagens e videos "ao vivo"
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


def change_res(width, heigth):
    # Funciona apenas para videos "ao vivo"
    capture.set(3, width)
    capture.set(4, heigth)


# img = cv.imread('./imgs/gato_grande.jpg')
# img_resized = resize(img, .5)
# cv.imshow('Cat', img)
# cv.imshow('Cat_resized', img_resized)
# cv.waitKey(0)

# Lendo frame por frame de um video e mostrando
capture = cv.VideoCapture('./video/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = resize(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video_maior', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
