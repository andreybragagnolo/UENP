# -*- coding: utf-8 -*-

import pygame
from threading import Thread, Lock

mutex = Lock()

class lobo:
    pos_x =0
    pos_y =0
    velocidade = 0
    imagem = None
    sentido = 0
    status = True
    tamanho_y = 80
    tamanho_x = 80
    
    def __init__(self, pos_x,pos_y, velocidade):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocidade = velocidade
        self.imagem = None
        self.sentido = 0;
        self.status = True
        self.tamanho_y = 80
        self.tamanho_x = 80
        
    def spawn_lobo(pos_x,pos_y, velocidade):
        mutex.acquire()
        try:
            l = lobo(pos_x,pos_y,velocidade)
            l.imagem = pygame.image.load('Lobo/cima1.png')
        finally:
            mutex.release()
        return l
    
    def wolf_up(vel, l) :
        l.pos_y -= vel
        l.imagem = pygame.image.load('Lobo/cima1.png')
        return l
    
    def wolf_down(vel, l):
        l.pos_y += vel
        l.imagem = pygame.image.load('Lobo/baixo1.png')
        return l
    
    def wolf_left(vel, l):
        mutex.acquire(1)
        try:
            l.pos_x -= vel
            l.imagem = pygame.image.load('Lobo/esquerda1.png')
        finally:
            mutex.release()
        return l
    
    def wolf_right(vel, l):
        mutex.acquire(1)
        try:
            l.pos_x += vel
            l.imagem = pygame.image.load('Lobo/direita1.png')
        finally:
            mutex.release()
        return l