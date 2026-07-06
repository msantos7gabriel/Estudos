import cv2 as cv

# Lendo frame por frame de um video e mostrando
capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()
    frame = cv.flip(frame, 1)
    frame = cv.resize(frame, (1280, 720), interpolation=cv.INTER_CUBIC)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # frame = cv.Canny(frame, 300, 325)
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
