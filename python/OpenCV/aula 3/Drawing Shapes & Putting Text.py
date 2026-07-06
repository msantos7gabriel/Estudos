import cv2 as cv
import numpy as np
from random import randint

blank = np.zeros((500, 500, 3), dtype='uint8')
# np.zeros(altura, largura, color_chanel)
# cv.imshow("Blank", blank)

# 1. Pintar a imagem um certo tipo de cor
blank[100:400, 100:400] = 0, 255, 0
# cv.imshow("RainBow", blank)
cv.waitKey(0)

# 2. Desenhar um Retângulo
cv.rectangle(blank, (100, 400), (blank.shape[1]//2, blank.shape[0]//2), (randint(0, 255),
             randint(0, 255), randint(0, 255)), thickness=cv.FILLED)

# 3. Desenhar um Circulo
cv.circle(blank, (blank.shape[1]//2,
          blank.shape[0]//2), 150, (0, 0, 255), thickness=-1)
# O Valor negativo tem o mesmo efeito do dv.FILLED

# 4. Desenhar uma linha
cv.line(blank, (400, 100), (
    blank.shape[1], blank.shape[0]), (255, 255, 255), thickness=3)

# 5. Inserir texto
cv.putText(blank, 'Bom dia', (100, 300),
           cv.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255), 2)
# posição/tipo de fonte/tamanho da fonte/cor/grossura

cv.imshow('tudo', blank)
cv.waitKey(0)
