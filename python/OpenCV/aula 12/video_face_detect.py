import cv2 as cv
from contextlib import contextmanager

@contextmanager
def video_capture(device_index):
    cap = cv.VideoCapture(device_index)
    try:
        yield cap
    finally:
        cap.release()

haar_cascade = cv.CascadeClassifier('aula 12\\haar_face.xml')

with video_capture(1) as capture:
    while True:
        isTrue, frame = capture.read()
        
        if not isTrue:
            break

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        flipped_frame = cv.flip(gray_frame, 1)

        faces_rect = haar_cascade.detectMultiScale(flipped_frame, scaleFactor=1.1, minNeighbors=3)

        for (x, y, w, h) in faces_rect:
            cv.rectangle(flipped_frame, (x + w, y + h), (x, y), (255, 255, 0), thickness=2)

        print(f'Número de faces encontradas: {len(faces_rect)}')

        cv.imshow('Video', flipped_frame)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break

cv.destroyAllWindows()
