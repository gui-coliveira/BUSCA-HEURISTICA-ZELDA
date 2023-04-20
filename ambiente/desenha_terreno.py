import pygame

def desenha_terreno(terreno_convertido, LINHAS, COLUNAS, GRAMA, AREIA, FLORESTA, MONTANHA, AGUA, TAMANHO_TILE, screen):
    
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            # Define a cor da célula com base no valor de custo
            if terreno_convertido[linha][coluna] == GRAMA:
                cor = (140, 211, 70)  # Verde para a grama
            elif terreno_convertido[linha][coluna] == AREIA:
                cor = (196, 188, 148)  # Amarelo para a areia
            elif terreno_convertido[linha][coluna] == FLORESTA:
                cor = (1, 115, 53)  # Verde escuro para a floresta
            elif terreno_convertido[linha][coluna] == MONTANHA:
                cor = (82, 70, 44)  # Cinza para a montanha
            elif terreno_convertido[linha][coluna] == AGUA:
                cor = (45, 72, 181)  # Azul para a água

            # Desenhar o tile na tela
            pygame.draw.rect(screen, cor, (coluna * TAMANHO_TILE,
                                        linha * TAMANHO_TILE, TAMANHO_TILE-1, TAMANHO_TILE-1))
