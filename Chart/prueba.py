import cv2

import numpy as np
import cv2

img = np.zeros((1000, 1000, 3), dtype=np.uint8)
print(img)

# recorremos cada uno de los elementos

for x in range(100):
    for y in range(100):
        # Cambiamos el color de cada uno de los pixeles de forma aleatoria
        img[x, y] = [0, 0, 0]

# guardamos la imagen png

cv2.imwrite("space.png", img)
