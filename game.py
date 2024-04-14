import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.85)
pygame.mixer.music.load('assets/music/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)
barulho_colisao = pygame.mixer.Sound('assets/music/smw_coin.wav')
barulho_colisao.set_volume(1)

largura = 800
altura = 600

altura_objeto = 40
largura_objeto = 40

x_cobra = largura / 2 - largura_objeto / 2
y_cobra = altura / 2 - altura_objeto / 2

x_controle = 5
y_controle = 0
velocidade = 5

x_maca = randint(0, largura - 40)
y_maca = randint(0, altura - 40)

tela = pygame.display.set_mode((largura, altura), HWSURFACE | DOUBLEBUF)
fonte = pygame.font.SysFont('arial', 40, True, True)
pontos = 0
pygame.display.set_caption('Game Test')
clock = pygame.time.Clock()

lista_cobra = []
comprimento_inicial = 0

morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x , y]
        #XeY[0] = x
        #XeY[1] = y

        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], altura_objeto, largura_objeto))

def reiniciar_jogo():
    global pontos,\
        comprimento_inicial,\
        x_cobra,\
        y_cobra,\
        x_maca,\
        y_maca,\
        lista_cobra,\
        lista_cabeca,\
        morreu
    pontos = 0
    comprimento_inicial = 0
    x_cobra = largura / 2 - largura_objeto / 2
    y_cobra = altura / 2 - altura_objeto / 2
    x_maca = randint(40, largura - 40)
    y_maca = randint(50, altura - 40)
    lista_cobra = []
    lista_cabeca = []
    morreu = False



while True:
    clock.tick(60)
    tela.fill((255, 255, 255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, largura_objeto, altura_objeto))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, largura_objeto, altura_objeto))

    if cobra.colliderect(maca):
        x_maca = randint(40, largura - 40)
        y_maca = randint(50, altura - 40)
        pontos = pontos + 1
        barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 10

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True)
        mensagem = 'Game over! Pressione a tecla: R para jogar novamente'
        texto_formatado = fonte2.render(mensagem,True, (0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (400, 40))
    pygame.display.update()
