# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 20:20:41 2021

@author: andy_
"""

class token:
    def __init__(self,nome, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.nome = nome


    def __init__(self):
        self.tipo = None
        self.valor = None
        self.nome = ""


def nextToken():
    global entrada
    global leitorPrevio
    global contador
    global EOF
    global saida
    
    contador = contador+1

    if contador == len(entrada):
        EOF = True
        return EOF
    else:
        if entrada[contador]!=' ':
            return entrada[contador]
        else:
            return nextToken()
            
            