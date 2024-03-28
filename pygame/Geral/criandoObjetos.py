import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')

red = 255
green = 255 
blue = 255
pos_x = 200
pos_y = 300
width = 40
height = 50

raio = 40

espessura = 5

inicio_x = 390
fim_x = 390
inicio_y = 0
fim_y = 600

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    #Criando um objeto no formato de retângulo na tela
    pygame.draw.rect(tela, (red,green,blue), (pos_x,pos_y,width,height))

    #Criando um objeto no formato de circulo na tela
    pygame.draw.circle(tela, (red,green,blue), (pos_x,pos_y), raio)
    
    #Criando uma linha na tela
    pygame.draw.line(tela, (red,green,blue), (inicio_x,inicio_y), (fim_x,fim_y), espessura)
    
    pygame.display.update()