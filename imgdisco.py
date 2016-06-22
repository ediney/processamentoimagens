# PROCESSAMENTO DE IMAGENS
# Trabalhando com uma imagem do disco
#
# Ediney dos Santos Lopes

import cv2
import numpy
import sys

# Leitura da imagem do disco
img = cv2.imread('pordosol.jpg')

# Dimensões da imagem
# Atributos: largura, altura e numero de canais
width, height, depth = img.shape
print height, width, depth

# Visualização da imagem na tela
cv2.imshow('OpenCV - Leitura de imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

