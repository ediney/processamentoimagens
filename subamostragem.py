# -*- coding: utf-8 -*-
# PROCESSAMENTO DE IMAGENS
# Subamostragem
#
# Ediney dos Santos Lopes

import cv2

psm='PonteSergioMota.jpg'
img1=cv2.imread(psm)
w=img1.shape[1]  
h=img1.shape[0]

# Subamostragem com o método de declinação Nearest-Neighbor
psm1=cv2.resize(img1,(w*4,h*1),interpolation=cv2.INTER_NEAREST)

# Subamostragem com o método de declinação Bilinear
psm2=cv2.resize(img1,(w*4,h*1),interpolation=cv2.INTER_LINEAR)

# Subamostragem com o método de declinação Bicubic
psm3=cv2.resize(img1,(w*4,h*1),interpolation=cv2.INTER_CUBIC)

# Subamostragem com o método de declinação Pixel Area
psm4=cv2.resize(img1,(w*4,h*1),interpolation=cv2.INTER_AREA)

# Visualização das telas da Ponte Sergio Mota
cv2.imshow('1 - Nearest-Neighbor',psm1)
cv2.imshow('2 - Bilinear',psm2)
cv2.imshow('3 - Bicubic',psm3)
cv2.imshow('4 - Pixel Area',psm4)

cv2.waitKey()
cv2.destroyAllWindows()

k=cv2.waitKey()
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):

    #Escrita de arquivos destino Ponte Sergio Mota
    cv2.imwrite('PonteSergioMotaIN.jpg', psm1)
    cv2.imwrite('PonteSergioMotaIL.jpg', psm2)
    cv2.imwrite('PonteSergioMotaIC.jpg', psm3)
    cv2.imwrite('PonteSergioMotaIA.jpg', psm4)

    cv2.destroyAllWindows()
