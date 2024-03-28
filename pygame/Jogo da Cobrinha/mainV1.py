import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#Declarando as Variaveis

#Musicas e Sons
pygame.mixer.music.set_volume(0.3) #Definindo o volume da musica de fundo
musicaFundo = pygame.mixer.music.load('taosmb3_ending.mp3')
musicaRecompensa = pygame.mixer.Sound("smw_1-up.wav")

#Tamanho Tela
largura = 640
altura = 480

#Tamanho Retangulo Vermelho
x_cobra = largura/2 
y_cobra = altura/2
lista_cobra = []


#Tamanho Retangulo Azul
x_maca = randint(40,600)
y_maca = randint(50,430)

#Fonte Utilizada
fonte = pygame.font.SysFont('arial', 20, True, False)
pontos = 0

#Fim da Declaração de variaveis#

#Iniciando a musica
# pygame.mixer.music.play(-1)

#Define o tamanho da tela
tela = pygame.display.set_mode((largura, altura))

#Definindo o titulo da tela
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

def aumentaCobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0],XeY[1],20,20))    

while True:
    relogio.tick(30)
    tela.fill((255,255,255)) #Definindo a cor da tela 
    mensagem = f'Pontos: {pontos}'
    textoFormatado = fonte.render(mensagem, True, (0,0,0)) #Escrevendo o texto na tela
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()     
    
    #Movimenta a posição da cobra    
    if pygame.key.get_pressed()[K_a]:
        x_cobra = x_cobra - 10
    elif pygame.key.get_pressed()[K_d]:
        x_cobra = x_cobra + 10
    elif pygame.key.get_pressed()[K_w]:
        y_cobra = y_cobra - 10
    elif pygame.key.get_pressed()[K_s]:
        y_cobra = y_cobra + 10
        
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        pontos = pontos + 1
        musicaRecompensa.play()
    
    #Armazenando a posição da cabeça da cobra em uma lista
    lista_cabeça = []
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)
    
    #Armazenando a posição da cobra em uma lista
    lista_cobra.append(lista_cabeça)
    
    aumentaCobra(lista_cobra)
    
    #Posição do texto
    tela.blit(textoFormatado, (480, 40))
    pygame.display.update()
