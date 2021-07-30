

import pygame
from threading import Thread, Lock

mutex = Lock()

class ovelha:
    pos_x =0
    pos_y =0
    velocidade = 0
    imagem = None
    tamanho_y = 50
    tamanho_x = 50
    status = True
    

    def __init__(self, pos_x,pos_y, velocidade):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocidade = velocidade
        self.imagem = None
        self.tamanho_y = 50
        self.tamanho_x = 50
        self.status = True
        
    def spawn_ovelha(pos_x,pos_y, velocidade):
        o = ovelha(pos_x,pos_y,velocidade)
        o.imagem = pygame.image.load('Animais/Ovelha/cima1.png')
        return o
    
    def sheep_up(vel, o):
        mutex.acquire(1)
        try:
            o.pos_y -= vel
            o.imagem = pygame.image.load('Animais/Ovelha/cima1.png')
        finally:
            mutex.release()
        return o
    
    def sheep_down(vel, o):
        o.pos_y += vel
        o.imagem = pygame.image.load('Animais/Ovelha/baixo1.png')
        return o
    
    def sheep_left(vel, o):
        o.pos_x -= vel
        o.imagem = pygame.image.load('Animais/Ovelha/esquerda1.png')
        return o
    
    def sheep_right(vel, o):
        o.pos_x += vel
        o.imagem = pygame.image.load('Animais/Ovelha/direita1.png')
        return o
    
    def Comer(o):
        o.pos_y -=5
        return o

