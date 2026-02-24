import pygame

# Submodulo, contém constantes e funções para o script
from pygame.locals import *

# Função para fechar a janela
from sys import exit

# importando randint para sortar valores dentro de um determinado intervalo
from random import randint

# inicializar todas as funções e variaveis do pygame
pygame.init()

# Musica de fundo

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('Bck.mp3')
pygame.mixer.music.play(-1)

# Som de colisão

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
barulho_colisao.set_volume(1)

# Objeto da tela 

largura = 900
altura = 600

# largura e altura do bloco

l_red = 20
a_red = 20

# Colocar o retangulo fique no meio da tela
x_cobra = largura/2
y_cobra = altura/2

x_maca = randint(40, 600)
y_maca = randint(50, 430)

# Criando variável para controlar a cobra só apertando

# Controle de velocidade

velocidade = 10

x_controle = velocidade
y_controle = 0


# Mesagem de morte

morreu = False

# Exibir testo na tela
pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, False)

# Definir a janela
tela = pygame.display.set_mode((largura, altura))

# Alterar o nome da janela
pygame.display.set_caption('Jogo')

# Objeto para controlar a velocidade (frames) do jogo.
relogio = pygame.time.Clock()

# Criar função para o corpo da cobra

def  aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y
        pygame.draw.rect(tela,(255,0,255), (XeY[0], XeY[1], 20, 20))

# Def para reiniciar o jogo
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cabeca, lista_cobra, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura/2)
    y_cobra = int(largura/2)
    lista_cabeca = []
    lista_cobra = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False

# Armazena a posição da cobra
lista_cobra = []

# Var do comprimento inicial

comprimento_inicial = 5

# Loop principal do jogo
while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    # Condição para detectar se ocorreu algum evento como tecla pressionada
    for  event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        # Evento para controlar o objeto apenas clicando

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = + velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = - velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == - velocidade:
                    pass
                else:
                    y_controle = + velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle


    '''
    # Evento para controlar o objeto pressionando
    if pygame.key.get_pressed()[K_a]:
        x_cobra = x_cobra - 20
    if pygame.key.get_pressed()[K_d]:
        x_cobra = x_cobra + 20
    if pygame.key.get_pressed()[K_w]:
        y_cobra = y_cobra - 20
    if pygame.key.get_pressed()[K_s]:
        y_cobra = y_cobra + 20'''

    # Desenhando um retângulo na tela
    # Pygame.desenhe.rect(retangulo)(na tela, (cor RGB), (local eixo x & y, largura e altura))
    cobra = pygame.draw.rect(tela, (255,0,255), (x_cobra,y_cobra,l_red,a_red))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))

    '''line_white_up = pygame.draw.line(tela, (255,255,255), (640,0),(0,0), 10)
    line_white_left = pygame.draw.line(tela, (255,255,255), (0,640), (0,0), 10)
    line_white_down = pygame.draw.line(tela, (255,255,255), (0,480), (640,480), 10)
    line_white_right = pygame.draw.line(tela, (255,255,255), (640,0), (640,480), 10)'''
    
    # condição para colisão
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 1
            
        
    # lista para criar o corpo
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    # Condição para se tiver mais de uma lista cabeça dentro da lista cobra
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('Arial', 100, True, False)
        fonte3 = pygame.font.SysFont('Arial', 20, True, False)
        mensagem2 = 'Press R to RESTART'
        mensagem = 'GAME OVER'
        texto_formatado2 = fonte3.render(mensagem2, True, (255,255,255))
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()
        ret_texto2 = texto_formatado2.get_rect()
        morreu = True
        while morreu:
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto2.center = (largura//2, altura//2)
            tela.blit(texto_formatado2, (370, 400))
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


        
    
    # Desenhando um circulo
    #pygame.draw.circle(tela,(0,0,255), (300, 260), 40)
    # Desenhando uma linha
    #pygame.draw.line(tela, (255,0,255), (390,0), (390,600), 5)
    tela.blit(texto_formatado, (700, 40))
    pygame.display.update()