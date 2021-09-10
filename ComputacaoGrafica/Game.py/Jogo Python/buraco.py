# -*- coding: utf-8 -*-

import pygame
import cachorro
class buraco:
    pos_x = 0
    pos_y = 0
    status = False
    imagem = None
    tamanho_x = 15
    tamanho_y = 15
    
    def __init__ (self, x, y):
        self.pos_x = x
        self.pos_y = y 
        self.status = False
        self.imagem = pygame.image.load('Buraco/buraco.png')
        self.tamanho_x = 50
        self.tamanho_y = 50
        
    def criarBuraco(cachorro, janela):
        b = buraco(cachorro.pos_x, cachorro.pos_y)
        print("Dog buraco ={} y={}" .format(cachorro.pos_x, cachorro.pos_y))
        janela.blit(pygame.image.load('Buraco/buraco.png'),(b.pos_x,b.pos_y))
        
        