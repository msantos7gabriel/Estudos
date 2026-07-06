# Comandos

## Comandos da aula 1

- **imread()** - Lê uma imagem de um arquivo.
- **imshow(nome-da-janela, imagem)** - Mostra a imagem em uma nova janela.
- **waitKey(x)** - Espera `x` milissegundos antes de fechar a janela. Se `x = 0`, a espera é indefinida até que uma tecla seja pressionada.
- **VideoCapture(int(0,1,2)/str(video_path))** - Captura vídeo de um arquivo ou de um dispositivo de câmera (0, 1, 2 correspondem aos diferentes dispositivos de câmera conectados).

### Leitura de vídeos e captura de frames

- **read()** - Lê o próximo frame de um vídeo ou da câmera.
  - Retorna dois valores:
    - `isTrue`: Booleano que indica se a leitura foi bem-sucedida.
    - `frame`: O frame atual capturado do vídeo.

### Exemplo básico

```python
capture = cv.VideoCapture(0)  # Captura do dispositivo de câmera

while True:
    isTrue, frame = capture.read()  # Lê frame por frame
    cv.imshow('Video', frame)  # Exibe o frame capturado

    if cv.waitKey(20) & 0xFF == ord('d'):  # Sai do loop ao pressionar 'd'
        break

capture.release()  # Libera a captura
cv.destroyAllWindows()  # Fecha todas as janelas abertas
```

### Comandos adicionais

- **release()** - Libera o vídeo/câmera, encerrando o uso do dispositivo ou arquivo.
- **destroyAllWindows()** - Fecha todas as janelas de exibição abertas pelo OpenCV.
- **0xFF** - Usado em conjunto com `ord()` para garantir que apenas o último byte da tecla pressionada seja considerado.

---

## Comandos da aula 2

### 1. **Função `resize()`**

```python
def resize(frame, scale=1):
    # Funciona para vídeos, imagens e vídeos ao vivo
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)
```

#### Explicação

- **Objetivo**: Redimensionar uma imagem ou frame de vídeo para uma nova escala.
- **Parâmetros**:
  - `frame`: Matriz de pixels que representa a imagem ou frame de vídeo.
  - `scale`: Fator de escala para redimensionar a imagem (padrão = 1, sem redimensionamento).

### Exemplo

```python
resized_frame = resize(frame, 0.5)  # Reduz o frame para 50% do tamanho original
```

---

### 2. **Função `change_res()`**

```python
def change_res(width, height):
    # Funciona apenas para vídeos ao vivo
    capture.set(3, width)
    capture.set(4, height)
```

#### Explicação

- **Objetivo**: Alterar a resolução de uma captura de vídeo ao vivo (de uma câmera).
- **Parâmetros**:
  - `width`: Largura da nova resolução.
  - `height`: Altura da nova resolução.

### Exemplo

```python
change_res(1280, 720)  # Altera a captura para resolução de 1280x720 pixels
```

---

## Comandos da aula 3

- **np.zeros(altura, largura, color_channel)** - Cria uma imagem em branco com as dimensões especificadas.
  - `altura`: Número de pixels em altura.
  - `largura`: Número de pixels em largura.
  - `color_channel`: Número de canais de cor (3 para RGB).

### Exemplo

```python
blank = np.zeros((500, 500, 3), dtype='uint8')  # Cria uma imagem em branco
```

---

- **blank[y1:y2, x1:x2] = (B, G, R)** - Pinta uma parte da imagem de uma cor específica.
  - `y1:y2, x1:x2`: Define as coordenadas da área a ser colorida.
  - `(B, G, R)`: Cor em formato BGR (azul, verde, vermelho).

### Exemplo

```python
blank[100:400, 100:400] = 0, 255, 0  # Pinta uma área de verde (0, 255, 0)
```

---

- **cv.rectangle(imagem, ponto_inicial, ponto_final, cor, thickness)** - Desenha um retângulo.
  - `imagem`: A matriz de imagem onde o retângulo será desenhado.
  - `ponto_inicial`: Coordenadas (x, y) do canto superior esquerdo.
  - `ponto_final`: Coordenadas (x, y) do canto inferior direito.
  - `cor`: Cor do retângulo em formato BGR.
  - `thickness`: Espessura da linha do retângulo. Se for `cv.FILLED` ou -1, o retângulo será preenchido.

### Exemplo

```python
cv.rectangle(blank, (100, 400), (blank.shape[1]//2, blank.shape[0]//2), (randint(0, 255), randint(0, 255), randint(0, 255)), thickness=cv.FILLED)
```

---

- **cv.circle(imagem, centro, raio, cor, thickness)** - Desenha um círculo.
  - `imagem`: A matriz de imagem onde o círculo será desenhado.
  - `centro`: Coordenadas (x, y) do centro do círculo.
  - `raio`: Raio do círculo.
  - `cor`: Cor do círculo em formato BGR.
  - `thickness`: Espessura da linha. Se for -1, o círculo será preenchido.

### Exemplo

```python
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 150, (0, 0, 255), thickness=-1)
```

---

- **cv.line(imagem, ponto_inicial, ponto_final, cor, thickness)** - Desenha uma linha.
  - `imagem`: A matriz de imagem onde a linha será desenhada.
  - `ponto_inicial`: Coordenadas (x, y) do ponto inicial.
  - `ponto_final`: Coordenadas (x, y) do ponto final.
  - `cor`: Cor da linha em formato BGR.
  - `thickness`: Espessura da linha.

### Exemplo

```python
cv.line(blank, (400, 100), (blank.shape[1], blank.shape[0]), (255, 255, 255), thickness=3)
```

---

- **cv.putText(imagem, texto, ponto_inicial, fonte, escala_fonte, cor, thickness)** - Insere um texto na imagem.
  - `imagem`: A matriz de imagem onde o texto será inserido.
  - `texto`: A string de texto a ser inserida.
  - `ponto_inicial`: Coordenadas (x, y) da posição do texto.
  - `fonte`: Tipo de fonte a ser utilizada (ex.: `cv.FONT_HERSHEY_TRIPLEX`).
  - `escala_fonte`: Tamanho da fonte.
  - `cor`: Cor do texto em formato BGR.
  - `thickness`: Espessura das letras.

### Exemplo

```python
cv.putText(blank, 'Bom dia', (100, 300), cv.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255), 2)
```

---

- **cv.imshow(nome-da-janela, imagem)** - Exibe a imagem.
  - `nome-da-janela`: Nome da janela onde a imagem será exibida.
  - `imagem`: A matriz de imagem.

### Exemplo

```python
cv.imshow('tudo', blank)
cv.waitKey(0)  # Espera até que uma tecla seja pressionada
```

---

## Comandos da aula 4

- **cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)** - Converte a imagem de BGR (padrão do OpenCV) para escala de cinza (grayscale).

### Exemplo

```python
cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Cinza', cinza)
```

---

- **cv.GaussianBlur(imagem, kernel, borda)** - Aplica um filtro de desfoque gaussiano (blur) na imagem.

### Exemplo

```python
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
```

---

- **cv.Canny(imagem, limite_inferior, limite_superior)** - Detecta bordas na imagem usando o algoritmo Canny.

### Exemplo

```python
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)
```

---

- **cv.dilate(imagem, kernel, iterations)** - Dilata a imagem, aumentando as áreas brancas (bordas).

### Exemplo

```python
dilated =

 cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)
```

---

- **cv.erode(imagem, kernel, iterations)** - Erosiona a imagem, reduzindo as áreas brancas (bordas).

### Exemplo

```python
eroded = cv.erode(dilated, (5, 5), iterations=2)
cv.imshow('Eroded', eroded)
```

---

- **cv.resize(imagem, dim, interpolation)** - Redimensiona a imagem para uma nova dimensão.

### Exemplo

```python
resized = cv.resize(img, (700, 700), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized', resized)
```

---

- **imagem[y1:y2, x1:x2]** - Recorta uma área da imagem de acordo com as coordenadas fornecidas.

### Exemplo

```python
cropped = img[0:350, 90:375]
cv.imshow('Cropped', cropped)
```

---

## Comandos da aula 5

- **cv.warpAffine(imagem, matriz, dim)** - Aplica uma transformação afim na imagem, como translação ou rotação.

---

### Função de Translação

Desloca a imagem para a esquerda, direita, cima ou baixo, de acordo com os valores de `x` e `y`.

```python
def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dim = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dim)
```

### Exemplo

```python
translated = translate(img, -100, -200)
cv.imshow('Imagem Deslocada', translated)
```

---

### Função de Rotação

Rotaciona a imagem de acordo com o ângulo fornecido.

```python
def rotate(img, angle, rotation_point=None):
    (height, width) = img.shape[:2]
    if rotation_point is None:
        rotation_point = (width // 2, height // 2)
    rot_mat = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dim = (width, height)
    return cv.warpAffine(img, rot_mat, dim)
```

### Exemplo

```python
rotated = rotate(img, -45)
cv.imshow('Imagem Rotacionada', rotated)
```

---

- **cv.flip(imagem, eixo)** - Espelha a imagem em torno de um eixo.

### Exemplo

```python
flip = cv.flip(img, 1)
cv.imshow('Imagem Espelhada', flip)
```

---

## Comandos da aula 6

- **cv.findContours(imagem, modo, método)** - Encontra os contornos de uma imagem.
  - `modo` pode ser:
    - `cv.RETR_TREE`: Detecta todos os contornos hierárquicos.
    - `cv.RETR_EXTERNAL`: Detecta apenas os contornos externos.
    - `cv.RETR_LIST`: Detecta todos os contornos sem hierarquia.
  - `método` pode ser:
    - `cv.CHAIN_APPROX_SIMPLE`: Reduz os pontos de contorno ao mínimo necessário.
    - `cv.CHAIN_APPROX_NONE`: Armazena todos os pontos de contorno.

### Exemplo

```python
contornos, hierarquia = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contornos)} contornos foram encontrados!')
```

---

- **cv.drawContours(imagem, contornos, índice, cor, espessura)** - Desenha os contornos encontrados em uma imagem.
  - `índice = -1`: Desenha todos os contornos.

### Exemplo

```python
cv.drawContours(blank, contornos, -1, (0, 0, 255), 1)
cv.imshow('Contornos desenhados', blank)
```

---

## Comandos da aula 7

- **cv.bitwise_and(imagem1, imagem2)**  
  Faz a operação lógica **AND** entre duas imagens binárias. Os pixels que são brancos em ambas as imagens permanecem brancos no resultado, enquanto todos os outros pixels são definidos como pretos.

  **Exemplo de uso**:

  ```python
  bitwise_and = cv.bitwise_and(circle, rectangle)
  cv.imshow('and', bitwise_and)
  ```

---

- **cv.bitwise_or(imagem1, imagem2)**  
  Faz a operação lógica **OR** entre duas imagens binárias. Aqui, os pixels que são brancos em pelo menos uma das imagens resultam em pixels brancos no resultado. Os outros pixels permanecem pretos.

  **Exemplo de uso**:

  ```python
  bitwise_or = cv.bitwise_or(rectangle, circle)
  cv.imshow('or', bitwise_or)
  ```

---

- **cv.bitwise_xor(imagem1, imagem2)**  
  Faz a operação lógica **XOR** entre duas imagens binárias. Os pixels que são brancos em apenas uma das imagens resultam em brancos no resultado. Se os pixels são brancos em ambas ou pretos em ambas as imagens, eles resultam em preto.

  **Exemplo de uso**:

  ```python
  bitwise_xor = cv.bitwise_xor(rectangle, circle)
  cv.imshow('xor', bitwise_xor)
  ```

---

- **cv.bitwise_not(imagem)**  
  Faz a operação lógica **NOT** em uma imagem binária, invertendo os valores dos pixels. Os pixels brancos tornam-se pretos e os pretos tornam-se brancos.

  **Exemplo de uso**:

  ```python
  bitwise_not = cv.bitwise_not(rectangle)
  cv.imshow('not', bitwise_not)
  ```

---

## Comandos da aula 8

- **cv.imread('caminho_da_imagem')**  
  Lê uma imagem de um arquivo especificado e a carrega na memória. O caminho da imagem deve ser fornecido corretamente para que a função possa acessá-la.

  **Exemplo de uso**:

  ```python
  img = cv.imread('imgs/gato.jpg')
  ```

---

- **cv.circle(imagem, centro, raio, cor, espessura)**  
  Desenha um círculo em uma imagem com o centro e o raio especificados. A cor e a espessura podem ser ajustadas, onde a espessura negativa (`thickness=-1`) preenche o círculo.

  **Exemplo de uso**:

  ```python
  mask = cv.circle(blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 200, 255, thickness=-1)
  ```

---

- **cv.bitwise_and(imagem1, imagem2, mask=mascara)**  
  Aplica a operação lógica **AND** em duas imagens (ou na mesma imagem) usando uma máscara opcional. Apenas os pixels onde a máscara é branca (valor 255) são mantidos.

  **Exemplo de uso**:

  ```python
  masked = cv.bitwise_and(img, img, mask=mask)
  ```

---

## Comandos da aula 9

- **cv.calcHist(imagens, canais, mascara, histSize, ranges)**  
  Calcula o histograma de uma imagem. Um histograma é uma representação gráfica da distribuição de intensidades de pixels em uma imagem, permitindo uma análise sobre o conteúdo da imagem.

  **Exemplo de uso**:

  ```python
  hist = cv.calcHist([img], [i], mask, [256], [0, 256])
  ```

---

- **plt.plot(dados, color)**  
  Plota uma série de dados em um gráfico. Neste caso, os dados do histograma são plotados para visualização.

  **Exemplo de uso**:

  ```python
  plt.plot(hist, color=col)
  ```

---

## Comandos da aula 10

- **cv.threshold(imagem, limite, valor_max, tipo_de_threshold)**  
  Aplica limiarização simples (thresholding) a uma imagem. O thresholding converte uma imagem em tons de cinza em uma imagem binária, onde os pixels são definidos como brancos (255) ou pretos (0) com base no limite escolhido.

  **Exemplo de uso**:

  ```python
  threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
  ```

---

- **cv.adaptiveThreshold(imagem, valor_max, método, tipo_de_threshold, tamanho_do_bloqueio, constante)**  
  Aplica a limiarização adaptativa (adaptive thresholding). Em vez de usar um único limite para toda a imagem, ele calcula o limite para pequenas regiões da imagem, tornando-o mais eficaz para imagens com iluminação não uniforme.

  **Exemplo de uso**:

  ```python
  adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 1)
  ```

---

## Comandos da aula 11

- **cv.Laplacian(imagem, profundidade)**  
  Aplica o operador de Laplace para detectar bordas em uma imagem. Este operador calcula as segundas derivadas das intensidades de pixel, detectando mudanças bruscas, ou seja, bordas.

  **Exemplo de uso**:

  ```python
  lap = cv.Laplacian(gray, cv.CV_64F)
  ```

---

- **cv.Sobel(imagem, profundidade, dx, dy)**  
  Aplica o operador de Sobel para detectar bordas em uma direção específica (horizontal ou vertical). O Sobel calcula a primeira derivada das intensidades de pixel, realçando as bordas de acordo com a direção escolhida.

  **Exemplo de uso**:

  ```python
  sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)  # Detecta bordas horizontais
  sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)  # Detecta bordas verticais
  ```

---

- **cv.Canny(imagem, limiar1, limiar2)**  
  Aplica o algoritmo de detecção de bordas Canny. Esse algoritmo detecta bordas ao procurar mudanças bruscas nas intensidades de pixel, usando dois limiares para identificar bordas fortes e fracas.

  **Exemplo de uso**:

  ```python
  canny = cv.Canny(gray, 150, 175)
  ```

---
