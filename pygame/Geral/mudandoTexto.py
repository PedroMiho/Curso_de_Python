import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#Declarando as Variaveis
#Tamanho Tela
largura = 640
altura = 480

#Tamanho Retangulo Vermelho
x = largura/2 
y = altura/2

#Tamanho Retangulo Azul
x_azul = randint(40,600)
y_azul = randint(50,430)

#Fonte Utilizada
fonte = pygame.font.SysFont('arial', 40, True, False)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    textoFormatado = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        # if event.type == KEYDOWN: #Caso o usuario Digite um botão
        #     if event.key == K_a:
        #         x = x - 20
        #     if event.key == K_d:
        #         x = x + 20
        #     if event.key == K_w:
        #         y = y - 20
        #     if event.key == K_s:
        #         y = y + 20
    
    if pygame.key.get_pressed()[K_a]:
        x = x - 10
    if pygame.key.get_pressed()[K_d]:
        x = x + 10
    if pygame.key.get_pressed()[K_w]:
        y = y - 10
    if pygame.key.get_pressed()[K_s]:
        y = y + 10
        
    retVermelho = pygame.draw.rect(tela, (255,0,0), (x,y,50,50))
    retAzul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50))
    
    if retVermelho.colliderect(retAzul):
        x_azul = randint(40,600)
        y_azul = randint(50,430)
        pontos = pontos + 1
        
    tela.blit(textoFormatado, (400, 40))
    pygame.display.update()
