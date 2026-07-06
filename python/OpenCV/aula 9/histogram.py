import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('imgs/gato.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

# grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

mask = cv.circle(
    blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 200, 255, thickness=-1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mascara', masked)

# grey_hist = cv.calcHist([grey], [0], mask, [256], [0, 256])

# plt.figure()
# plt.title('Grey Scale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of Pixels ')
# plt.plot(grey_hist)
# plt.xlim([0, 256])
# plt.show()


# Color histogram
plt.figure()
plt.title('Color Scale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels ')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
