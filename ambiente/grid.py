import pygame
import math

# Definir as cores dos diferentes tipos de terreno
GRAMA = (124, 252, 0)
AREIA = (244, 164, 96)
FLORESTA = (34, 139, 34)
MONTANHA = (139, 137, 137)
AGUA = (30, 144, 255)

# Definir o custo de cada tipo de terreno
CUSTO = {
    GRAMA: 10,
    AREIA: 20,
    FLORESTA: 100,
    MONTANHA: 150,
    AGUA: 180
}

# Inicializar o pygame
pygame.init()

# Definir as dimensões da tela e o tamanho dos tiles
LARGURA_TELA = 250
ALTURA_TELA = 250
TAMANHO_TILE = 50

# Criar a janela
screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Definir as dimensões da matriz do terreno
LINHAS = 5
COLUNAS = 5

# Definir o terreno manualmente
terreno = [
    [GRAMA, GRAMA, GRAMA, AGUA, AGUA],
    [GRAMA, AREIA, GRAMA, AGUA, AGUA],
    [GRAMA, AREIA, FLORESTA, FLORESTA, AGUA],
    [GRAMA, GRAMA, MONTANHA, FLORESTA, AGUA],
    [MONTANHA, MONTANHA, MONTANHA, GRAMA, GRAMA]
]

# Definir a fonte do texto
fonte = pygame.font.SysFont(None, 18)

# Loop principal do jogo
while True:
    # Capturar os eventos do pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Desenhar o terreno na tela
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            # Define a cor da célula com base no valor de custo
            if terreno[linha][coluna] == GRAMA:
                cor = (34, 177, 76)  # Verde para a grama
            elif terreno[linha][coluna] == AREIA:
                cor = (255, 255, 102)  # Amarelo para a areia
            elif terreno[linha][coluna] == FLORESTA:
                cor = (0, 102, 0)  # Verde escuro para a floresta
            elif terreno[linha][coluna] == MONTANHA:
                cor = (64, 64, 64)  # Cinza para a montanha
            elif terreno[linha][coluna] == AGUA:
                cor = (0, 0, 255)  # Azul para a água
            
            # Desenhar o tile na tela
            pygame.draw.rect(screen, cor, (coluna * TAMANHO_TILE, linha * TAMANHO_TILE, TAMANHO_TILE, TAMANHO_TILE))

    # Atualizar a tela
    pygame.display.update()
