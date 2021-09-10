# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:49:41 2021

@author: andy_
"""

from threading import Thread
import time


def carrinho(velocidade,nome):
    distancia = 0
    while distancia <= 1000:
        print("Carrinho :",nome,distancia)
        distancia += velocidade
        time.sleep(0.3)



carrinho1 = Thread(target=carrinho,args=[1.1,"Ed"])
carrinho2 = Thread(target=carrinho,args=[1.2,"Paulo"])


carrinho1.start()
carrinho2.start()