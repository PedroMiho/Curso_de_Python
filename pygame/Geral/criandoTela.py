import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')

#Criando um Loop Infinito para o funcionamento do jogo 
while True:
    
    #Colocando um evento de click num loop for para saida do jogo
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    #Atualizando a janela do jogo a cada iteração
    pygame.display.update()