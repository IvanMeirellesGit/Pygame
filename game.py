import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
altura_objeto = 40
largura_objeto = 50
x = largura / 2 - largura_objeto / 2
y = altura / 2 - altura_objeto / 2
x_azul = randint(40, 600)
y_azul = randint(50, 430)

tela = pygame.display.set_mode((largura, altura), HWSURFACE | DOUBLEBUF)
fonte = pygame.font.SysFont('arial', 40, True, True)
pontos = 0
pygame.display.set_caption('Game Test')
clock = pygame.time.Clock()

while True:
    clock.tick(40)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20 
        '''
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    ret_verde = pygame.draw.rect(tela, (0, 255, 0), (x, y, largura_objeto, altura_objeto))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))

    if ret_verde.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = pontos + 1
    tela.blit(texto_formatado, (400, 40))
    pygame.display.update()
