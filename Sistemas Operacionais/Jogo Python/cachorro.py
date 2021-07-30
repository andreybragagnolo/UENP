# -*- coding: utf-8 -*-

import pygame
from threading import Lock

mutex = Lock()

class cachorro:
    pos_x=0
    pos_y=0
    imagem = None
    power_level = 0
    buracos = [3]
    listaBuracos = []
    tamanho_y = 60
    tamanho_x = 60
    
    
    
    
    def __init__(self, pos_x,pos_y,power_level):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.power_level = power_level
        self.quantidadeBuracos = 0
        self.listaBuracos = [power_level]
        self.tamanho_y = 40
        self.tamanho_x = 40
        

    def spawn_dog(x, y, p_level):
        c = cachorro(x,y,p_level)
        c.imagem = pygame.image.load('Cachorro/caoBaixo.png')
        return c
    
    def dog_up(vel, c):
        mutex.acquire(1)
        try:
            c.pos_y -= vel
            c.imagem = pygame.image.load('Cachorro/caoCima.png')
        finally:
            mutex.release()
        return c
    
    def dog_down(vel, c):
        mutex.acquire(1)
        try:
            c.pos_y += vel
            c.imagem = pygame.image.load('Cachorro/caoBaixo.png')
        finally:
            mutex.release()
        return c
    
    def dog_left(vel, c):
        mutex.acquire(1)
        try:
            c.pos_x -= vel
            c.imagem = pygame.image.load('Cachorro/caoEsquerda.png')
        finally:
            mutex.release()
        return c
    
    def dog_right(vel, c):
        mutex.acquire(1)
        try:
            c.pos_x += vel
            c.imagem = pygame.image.load('Cachorro/caoDireita.png')
        finally:
            mutex.release()
        return c
    
    def dog_buraco(c):
        c.quantidadeBuracos +=1
        c.buracos.append(c.pos_x)
        c.buracos.append(c.pos_y)
        c.listaBuracos.append(c.buracos) 
        return c
