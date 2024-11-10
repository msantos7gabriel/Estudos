import os
import cv2 as cv
import numpy as np

people = []
for i in os.listdir(r'aula 13\Faces\train'):
    people.append(i)
DIR = r'aula 13\Faces\train'
haar_cascade = cv.CascadeClassifier(r'aula 12/haar_face.xml')


features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = person.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=3)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print('Training done ---------------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Treinar o reconhecimento sobre os recurso e a lista de rótulos
face_recognizer.train(features, labels)

print(os.getcwd())
# np.save('aula 13\labels.npy', labels)
# np.save('features.npy', features)
