import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Defina as variáveis do jogo
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

paddle_width = 20
paddle_height = 100
left_paddle_y = SCREEN_HEIGHT // 2 - paddle_height // 2
right_paddle_y = SCREEN_HEIGHT // 2 - paddle_height // 2
paddle_speed = 5

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimentação das barras
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s]:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP]:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        right_paddle_y += paddle_speed

    # Movimentação da bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Verifique colisões com as paredes
    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y

    # Verifique colisão com as barras
    if ball_x <= paddle_width and left_paddle_y < ball_y < left_paddle_y + paddle_height:
        ball_speed_x = -ball_speed_x
    elif ball_x >= SCREEN_WIDTH - paddle_width and right_paddle_y < ball_y < right_paddle_y + paddle_height:
        ball_speed_x = -ball_speed_x

    # Verifique se a bola saiu da tela
    if ball_x < 0 or ball_x > SCREEN_WIDTH:
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2

    # Limpe a tela
    screen.fill(BLACK)

    # Desenhe as barras
    pygame.draw.rect(screen, WHITE, pygame.Rect(10, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, pygame.Rect(SCREEN_WIDTH - 30, right_paddle_y, paddle_width, paddle_height))

    # Desenhe a bola
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 10)

    # Atualize a tela
    pygame.display.flip()

    # Limita a taxa de quadros por segundo
    pygame.time.Clock().tick(60)
