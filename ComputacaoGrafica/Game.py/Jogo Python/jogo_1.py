# -*- coding: utf-8 -*-

from cachorro import cachorro
from ovelha import ovelha
from lobo import lobo
import pygame
from random import randint
from threading import Thread, Lock
from ThreadComRetorno import ThreadComRetorno
from buraco import buraco



x = 400
y = 300
speed = 10
timer = 0
tempo_segundo = 0
mutex = Lock()

pygame.init()

#Criação dos elementos do jogo -> Ovelhas, Lobos, elementos de cenário e outros
fundo = pygame.image.load('FUNDO.png')
cachorro1 = cachorro.spawn_dog(x,y,3)
tarefalobo = ThreadComRetorno(target = lobo.spawn_lobo, args = [1,150,4])
tarefalobo.start()
lobo1 = tarefalobo.join()
tarefalobo = ThreadComRetorno(target = lobo.spawn_lobo, args = [1,300,3])
tarefalobo.start()
lobo2 = tarefalobo.join()
tarefalobo = ThreadComRetorno(target = lobo.spawn_lobo, args = [1,450,3])
tarefalobo.start()
lobo3 = tarefalobo.join()
tarefalobo = ThreadComRetorno(target = lobo.spawn_lobo, args = [1,randint(150,450),10])
tarefalobo.start()
lobo4 = tarefalobo.join()
lobo4.tamanho_x, lobo4.tamanho_y = 90,90
lobo4.status = False


buraco1 = buraco( randint(100, 720) ,randint(150, 500))
buraco1.status = False


ovelha1 = ovelha.spawn_ovelha(620,530,4)
ovelha2 = ovelha.spawn_ovelha(360,530,3)
ovelha3 = ovelha.spawn_ovelha(140,530,1)


window = pygame.display.set_mode((800,600))
som_ponto = pygame.mixer.Sound('ponto.wav')

#criação dos elementos de texto - Score e Tempo
font = pygame.font.SysFont('arial black', 11)
texto = font.render(" Tempo: ", True, (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center= (35,35)
Score = 0

fontScore = pygame.font.SysFont('arial black', 11)
textoScore = font.render(" Score ", True, (0,0,0))
pos_textoScore = textoScore.get_rect()
pos_textoScore.center= (30,50)

open_window = True
listaBuracos = []



while open_window:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        #Fechar a janela pelo "X" no canto superior 
        if event.type == pygame.QUIT:
            open_window = False
    #recebe uma entrada do teclado 
    
    comand = pygame.key.get_pressed()
    
    if comand[pygame.K_w]:
        movimentaCachorro = Thread(target = cachorro.dog_up, args =[speed, cachorro1])
        movimentaCachorro.start()
        
    if comand[pygame.K_s]:
        movimentaCachorro = Thread(target = cachorro.dog_down, args =[speed, cachorro1])
        movimentaCachorro.start()
        
    if comand[pygame.K_a]:
        movimentaCachorro = Thread(target = cachorro.dog_left, args =[speed, cachorro1])
        movimentaCachorro.start()
    if comand[pygame.K_d]:
        movimentaCachorro = Thread(target = cachorro.dog_right, args =[speed, cachorro1])
        movimentaCachorro.start()
        

    
    #Define a limitação de posição das ovelhas -> Se chegarem à 100, aumenta-se o score
    if ovelha1.pos_y>100:
        movimento_ovelha = Thread(target = ovelha.sheep_up, args = [ovelha1.velocidade,ovelha1])
        movimento_ovelha.start()

    else:
        som_ponto.play();
        Score+=1
        ovelha1 = ovelha.spawn_ovelha(620,530,2)
        
    if ovelha2.pos_y>100:
        movimento_ovelha2 = Thread(target = ovelha.sheep_up, args = [ovelha2.velocidade,ovelha2])
        movimento_ovelha2.start()
    else:
        som_ponto.play();
        Score+=1
        ovelha2 = ovelha.spawn_ovelha(360,530,3)

    if ovelha3.pos_y>100:
        movimento_ovelha3 = Thread(target = ovelha.sheep_up, args = [ovelha3.velocidade,ovelha3])
        movimento_ovelha3.start()
    
    else:
        som_ponto.play();
        Score+=1
        ovelha3 = ovelha.spawn_ovelha(140,530,1)

# Limita as posições dos lobos
    if (((lobo1.sentido == 0) and (lobo1.pos_x>=0 and lobo1.pos_x<=770))):
        movimentaLobo1 = Thread(target = lobo.wolf_right, args =[lobo1.velocidade, lobo1])
        movimentaLobo1.start()
        lobo1.sentido = 0
    elif lobo1.pos_x>0:
        movimentaLobo1 = Thread(target = lobo.wolf_left, args =[lobo1.velocidade, lobo1])
        movimentaLobo1.start()
        lobo1.sentido = 1
    else:
        movimentaLobo1 = Thread(target = lobo.wolf_right, args =[lobo1.velocidade, lobo1])
        movimentaLobo1.start()
        lobo1.sentido = 0
        
    if (((lobo2.sentido == 0) and (lobo2.pos_x>=0 and lobo2.pos_x<=770))):
        movimentaLobo2 = Thread(target = lobo.wolf_right, args =[lobo2.velocidade, lobo2])
        movimentaLobo2.start()
        lobo2.sentido = 0
    elif lobo2.pos_x>0:
        movimentaLobo2 = Thread(target = lobo.wolf_left, args =[lobo2.velocidade, lobo2])
        movimentaLobo2.start()
        lobo2.sentido = 1
    else:
        movimentaLobo2 = Thread(target = lobo.wolf_right, args =[lobo2.velocidade, lobo2])
        movimentaLobo2.start()
        lobo2.sentido = 0
    if (((lobo3.sentido == 0) and (lobo3.pos_x>=0 and lobo3.pos_x<=770))):
        movimentaLobo3 = Thread(target = lobo.wolf_right, args =[lobo3.velocidade, lobo3])
        movimentaLobo3.start()
        lobo3.sentido = 0
    elif lobo3.pos_x>0:
        movimentaLobo3 = Thread(target = lobo.wolf_left, args =[lobo3.velocidade, lobo3])
        movimentaLobo3.start()
        lobo3.sentido = 1
    else:
        movimentaLobo3 = Thread(target = lobo.wolf_left, args =[lobo3.velocidade, lobo3])
        movimentaLobo3.start()
        lobo3.sentido = 0
        
    if (((lobo4.sentido == 0) and (lobo4.pos_x>=0 and lobo4.pos_x<=770))):
        movimentaLobo4 = Thread(target = lobo.wolf_right, args =[lobo4.velocidade, lobo4])
        movimentaLobo4.start()
        lobo4.sentido = 0
    elif lobo4.pos_x>0:
        movimentaLobo4 = Thread(target = lobo.wolf_left, args =[lobo4.velocidade, lobo4])
        movimentaLobo4.start()
        lobo4.sentido = 1
    else:
        movimentaLobo4 = Thread(target = lobo.wolf_right, args =[lobo4.velocidade, lobo4])
        movimentaLobo4.start()
        lobo4.sentido = 0


    if (timer <20):
        timer +=1

    else:
        tempo_segundo += 1
        textoScore = font.render(" Score:"+str(Score), True, (0,0,0))
        texto = font.render(" Tempo:"+str(tempo_segundo), True, (0,0,0))
        timer = 0
        

    window.fill((0,0,0))
    window.blit(fundo, (0,0)) 
    window.blit(textoScore, pos_textoScore)
    window.blit(texto,pos_texto)

    #Limita a posição do cachorro
    if cachorro1.pos_x<=0:
        cachorro1.pos_x = 5
    if cachorro1.pos_x>=790:
        cachorro1.pos_x = 790
    if cachorro1.pos_y>=590:
        cachorro1.pos_y = 590
    if cachorro1.pos_y<=0:
        cachorro1.pos_y = 5

    #define o "hitbox" do cão
    if ((cachorro1.pos_x-cachorro1.tamanho_x>=lobo1.pos_x-lobo1.tamanho_x)and (cachorro1.pos_x+cachorro1.tamanho_x<=lobo1.pos_x+lobo1.tamanho_x)):
        if ((cachorro1.pos_y-cachorro1.tamanho_y>=lobo1.pos_y-lobo1.tamanho_y)and (cachorro1.pos_y+cachorro1.tamanho_y<=lobo1.pos_y+lobo1.tamanho_y)):
            Score+=1
            lobo1.status = False
    if ((cachorro1.pos_x-cachorro1.tamanho_x>=lobo2.pos_x-lobo2.tamanho_x)and(cachorro1.pos_x+cachorro1.tamanho_x<=lobo2.pos_x+lobo2.tamanho_x)):
        if ((cachorro1.pos_y-cachorro1.tamanho_y>=lobo2.pos_y-lobo2.tamanho_y)and (cachorro1.pos_y+cachorro1.tamanho_y<=lobo2.pos_y+lobo2.tamanho_y)):
            Score+=1
            lobo2.status = False
    if ((cachorro1.pos_x-cachorro1.tamanho_x>=lobo3.pos_x-lobo3.tamanho_x)and(cachorro1.pos_x+cachorro1.tamanho_x<=lobo3.pos_x+lobo3.tamanho_x)):
        if ((cachorro1.pos_y-cachorro1.tamanho_y>=lobo3.pos_y-lobo3.tamanho_y)and (cachorro1.pos_y+cachorro1.tamanho_y<=lobo3.pos_y+lobo3.tamanho_y)):
            lobo3.status = False
            Score+=1
            
    if lobo4.status == True:        
        if ((cachorro1.pos_x-cachorro1.tamanho_x>=lobo4.pos_x-lobo4.tamanho_x)and(cachorro1.pos_x+cachorro1.tamanho_x<=lobo4.pos_x+lobo4.tamanho_x)):
            if ((cachorro1.pos_y-cachorro1.tamanho_y>=lobo4.pos_y-lobo4.tamanho_y)and (cachorro1.pos_y+cachorro1.tamanho_y<=lobo4.pos_y+lobo4.tamanho_y)):
                lobo4.status = False
                Score+=1

            
    ########### OVELHA 1 -> Hitbox  
    if ((ovelha1.pos_x-ovelha1.tamanho_x>=lobo1.pos_x-lobo1.tamanho_x) and(ovelha1.pos_x+ovelha1.tamanho_x<=lobo1.pos_x+lobo1.tamanho_x)):
        if ((ovelha1.pos_y-ovelha1.tamanho_y>=lobo1.pos_y-lobo1.tamanho_y) and(ovelha1.pos_y+ovelha1.tamanho_y<=lobo1.pos_y+lobo1.tamanho_y)):
            ovelha1.status = False

    
    if ((ovelha1.pos_x-ovelha1.tamanho_x>=lobo2.pos_x-lobo2.tamanho_x) and(ovelha1.pos_x+ovelha1.tamanho_x<=lobo2.pos_x+lobo2.tamanho_x)):
        if ((ovelha1.pos_y-ovelha1.tamanho_y>=lobo2.pos_y-lobo2.tamanho_y) and(ovelha1.pos_y+ovelha1.tamanho_y<=lobo2.pos_y+lobo2.tamanho_y)):
            ovelha1.status = False

    if ((ovelha1.pos_x-ovelha1.tamanho_x>=lobo3.pos_x-lobo3.tamanho_x) and(ovelha1.pos_x+ovelha1.tamanho_x<=lobo3.pos_x+lobo3.tamanho_x)):
        if ((ovelha1.pos_y-ovelha1.tamanho_y>=lobo3.pos_y-lobo3.tamanho_y) and(ovelha1.pos_y+ovelha1.tamanho_y<=lobo3.pos_y+lobo3.tamanho_y)):
            ovelha1.status = False
    if (lobo4.status):
        if ((ovelha1.pos_x-ovelha1.tamanho_x>=lobo4.pos_x-lobo4.tamanho_x) and(ovelha1.pos_x+ovelha1.tamanho_x<=lobo4.pos_x+lobo4.tamanho_x)):
            if ((ovelha1.pos_y-ovelha1.tamanho_y>=lobo4.pos_y-lobo4.tamanho_y) and(ovelha1.pos_y+ovelha1.tamanho_y<=lobo4.pos_y+lobo4.tamanho_y)):
                ovelha1.status = False


     
    ########### OVELHA 2 -> Hitbox    
    if ((ovelha2.pos_x-ovelha2.tamanho_x>=lobo1.pos_x-lobo1.tamanho_x) and(ovelha2.pos_x+ovelha2.tamanho_x<=lobo1.pos_x+lobo1.tamanho_x)):
        if ((ovelha2.pos_y-ovelha2.tamanho_y>=lobo1.pos_y-lobo1.tamanho_y) and(ovelha2.pos_y+ovelha2.tamanho_y<=lobo1.pos_y+lobo1.tamanho_y)):
            ovelha2.status = False

            
    if ((ovelha2.pos_x-ovelha2.tamanho_x>=lobo2.pos_x-lobo2.tamanho_x) and(ovelha2.pos_x+ovelha2.tamanho_x<=lobo2.pos_x+lobo2.tamanho_x)):
        if ((ovelha2.pos_y-ovelha2.tamanho_y>=lobo2.pos_y-lobo2.tamanho_y) and(ovelha2.pos_y+ovelha2.tamanho_y<=lobo2.pos_y+lobo2.tamanho_y)):
            ovelha2.status = False

    if ((ovelha2.pos_x-ovelha2.tamanho_x>=lobo3.pos_x-lobo3.tamanho_x) and(ovelha2.pos_x+ovelha2.tamanho_x<=lobo3.pos_x+lobo3.tamanho_x)):
        if ((ovelha2.pos_y-ovelha2.tamanho_y>=lobo3.pos_y-lobo3.tamanho_y) and(ovelha2.pos_y+ovelha2.tamanho_y<=lobo3.pos_y+lobo3.tamanho_y)):
            ovelha2.status = False
    
    if (lobo4.status):
        if ((ovelha2.pos_x-ovelha2.tamanho_x>=lobo4.pos_x-lobo4.tamanho_x) and(ovelha2.pos_x+ovelha2.tamanho_x<=lobo4.pos_x+lobo4.tamanho_x)):
            if ((ovelha2.pos_y-ovelha2.tamanho_y>=lobo4.pos_y-lobo4.tamanho_y) and(ovelha2.pos_y+ovelha2.tamanho_y<=lobo4.pos_y+lobo4.tamanho_y)):
                ovelha2.status = False


            
    ########## OVELHA 3 -> Hitbox
    if ((ovelha3.pos_x-ovelha3.tamanho_x>=lobo1.pos_x-lobo1.tamanho_x) and (ovelha3.pos_x+ovelha3.tamanho_x<=lobo1.pos_x+lobo1.tamanho_x)):
        if ((ovelha3.pos_y-ovelha3.tamanho_y>=lobo1.pos_y-lobo1.tamanho_y) and(ovelha3.pos_y+ovelha3.tamanho_y<=lobo1.pos_y+lobo1.tamanho_y)):
            ovelha3.status = False

    if ((ovelha3.pos_x-ovelha3.tamanho_x>=lobo2.pos_x-lobo2.tamanho_x) and(ovelha3.pos_x+ovelha3.tamanho_x<=lobo2.pos_x+lobo2.tamanho_x)):
        if ((ovelha3.pos_y-ovelha3.tamanho_y>=lobo2.pos_y-lobo2.tamanho_y) and(ovelha3.pos_y+ovelha3.tamanho_y<=lobo2.pos_y+lobo2.tamanho_y)):
            ovelha3.status = False

    if ((ovelha3.pos_x-ovelha3.tamanho_x>=lobo3.pos_x-lobo3.tamanho_x) and(ovelha3.pos_x+ovelha3.tamanho_x<=lobo3.pos_x+lobo3.tamanho_x)):
        if ((ovelha3.pos_y-ovelha3.tamanho_y>=lobo3.pos_y-lobo3.tamanho_y) and(ovelha3.pos_y+ovelha3.tamanho_y<=lobo3.pos_y+lobo3.tamanho_y)):
            ovelha3.status = False
    
    if (lobo4.status):
        if ((ovelha3.pos_x-ovelha3.tamanho_x>=lobo4.pos_x-lobo4.tamanho_x) and(ovelha3.pos_x+ovelha3.tamanho_x<=lobo4.pos_x+lobo4.tamanho_x)):
            if ((ovelha3.pos_y-ovelha3.tamanho_y>=lobo4.pos_y-lobo4.tamanho_y) and(ovelha3.pos_y+ovelha3.tamanho_y<=lobo4.pos_y+lobo4.tamanho_y)):
                ovelha3.status = False


            
       
    
   #renderização dos diversos elementos da tela (Ovelhas, cachorro, e outros)    
    window.blit(cachorro1.imagem,(cachorro1.pos_x,cachorro1.pos_y))
################### Ovelhas -> Renascer 
    if ovelha1.status:
        window.blit(ovelha1.imagem,(ovelha1.pos_x,ovelha1.pos_y))
    
    if ovelha2.status:
        window.blit(ovelha2.imagem,(ovelha2.pos_x,ovelha2.pos_y))
    
    if ovelha3.status:
        window.blit(ovelha3.imagem,(ovelha3.pos_x,ovelha3.pos_y))
    
############################# LOBOS -> Renascer    
    if lobo1.status:
        window.blit(lobo1.imagem,(lobo1.pos_x,lobo1.pos_y))
    else:
        if tempo_segundo%3 == 0:
            tarefalobo = ThreadComRetorno(target = lobo.spawn_lobo, args=[1,randint(120,250),randint(1,5)])
            tarefalobo.start()
            lobo1 = tarefalobo.join()

     
    if lobo2.status:
        window.blit(lobo2.imagem,(lobo2.pos_x,lobo2.pos_y))

    else:
        if tempo_segundo%4 == 0:
            lobo2 = lobo.spawn_lobo(1,randint(251,430),randint(1,5))


    if lobo3.status:
        window.blit(lobo3.imagem,(lobo3.pos_x,lobo3.pos_y))
    else:
        if tempo_segundo%5 == 0:
            lobo3 = lobo.spawn_lobo(1,randint(431,580),randint(1,5))
            
    if lobo4.status:
        window.blit(lobo4.imagem,(lobo4.pos_x,lobo4.pos_y))
    else:
        if tempo_segundo%15 == 0:
            lobo4 = lobo.spawn_lobo(1,randint(150,580),8)
            lobo4.status = False
    
    if lobo4.status == False:
        if Score > 100 and tempo_segundo%15==0:
            lobo4.status = True
        else:
            lobo4.status = False
            
            
########################### BURACOS
    if (len(listaBuracos)>0):
        
        for item in listaBuracos:
            
            if ((cachorro1.pos_x-cachorro1.tamanho_x>=item.pos_x-item.tamanho_x)and(cachorro1.pos_x+cachorro1.tamanho_x<=item.pos_x+item.tamanho_x)):
                if ((cachorro1.pos_y-cachorro1.tamanho_y>=item.pos_y-item.tamanho_y)and (cachorro1.pos_y+cachorro1.tamanho_y<=item.pos_y+item.tamanho_y)):
                    Score -= 10
                    
    
    if (Score>=10) and (tempo_segundo%10==0) and (buraco1.status == False):
        if timer ==0:
            buraco1.status = True
            listaBuracos.append(buraco1)
            buraco1 = buraco( randint(100, 720) ,randint(150, 500))
            buraco1.status = False

    if (len(listaBuracos) > 0):
            for item in listaBuracos:
                window.blit(item.imagem, (item.pos_x,item.pos_y))
    
    if Score<0:
            window.blit(pygame.image.load('game_over.png'), (400,300))
            mutex.acquire(25000)
            mutex.release()
    else:
        pygame.display.update()
pygame.quit()


def criar_ovelha(x,y,velocidade):
    objeto_ovelha = ovelha.spawn_ovelha(620,530,2)
    return objeto_ovelha