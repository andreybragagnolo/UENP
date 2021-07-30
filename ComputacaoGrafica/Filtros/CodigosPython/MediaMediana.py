# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:21:54 2021

@author: andy_
"""

import cv2
import numpy as np

imagem = cv2.imread('ovelhateste.jpg')

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

imagem2 = cv2.meanBlur(imagem, (4,4))
cv2.imwrite('ovelhaJanela4.jpg', imagem2) 

imagem3 = cv2.meanBlur(imagem, (9,9))
cv2.imwrite('ovelhaJanela9.jpg', imagem3)


suave_mediana = np.vstack([
    np.hstack([imagem,
               cv2.medianBlur(imagem,3)]),
    np.hstack([cv2.medianBlur(imagem,5), 
               cv2.medianBlur(imagem,7)]),
    np.hstack([cv2.medianBlur(imagem,9),
               cv2.medianBlur(imagem,11)])]
    )

cv2.imwrite('ovelhaMedianaDiversos.jpg', suave_mediana)
