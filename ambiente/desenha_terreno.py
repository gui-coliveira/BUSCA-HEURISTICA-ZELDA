import pygame


def desenha_terreno(terreno_convertido, LINHAS, COLUNAS, GRAMA, AREIA, FLORESTA, MONTANHA, AGUA, PRETO, BRANCO, AMARELO,
                    TAMANHO_TILE, screen, portaaberta, telaFinal):

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
            elif terreno_convertido[linha][coluna] == PRETO:
                cor = (0, 0, 0)  # PRETO
            elif terreno_convertido[linha][coluna] == BRANCO:
                cor = (255, 255, 255)  # BRANCO
            elif terreno_convertido[linha][coluna] == AMARELO:
                cor = (201, 176, 10)  # AMARELO

            # Desenhar o tile na tela
            pygame.draw.rect(screen, cor, (coluna * TAMANHO_TILE,
                                           linha * TAMANHO_TILE, TAMANHO_TILE-1, TAMANHO_TILE-1))
        if telaFinal == False:
            # Carregar a imagem
            imagem_espada = pygame.image.load('./img/sword.png')

            # Redimensionar a imagem
            imagem_redimensionada_espada = pygame.transform.scale(
                imagem_espada, (TAMANHO_TILE, TAMANHO_TILE))

            # Desenhar a imagem na célula (x, y)
            screen.blit(imagem_redimensionada_espada,
                        (2*TAMANHO_TILE, 1*TAMANHO_TILE))

            # Carregar a imagem
            imagem_door = pygame.image.load('./img/door.png')
            imagem_dooropen = pygame.image.load('./img/door_open.png')

            # Redimensionar a imagem
            imagem_redimensionada_door = pygame.transform.scale(
                imagem_door, (TAMANHO_TILE, TAMANHO_TILE))
            imagem_redimensionada_dooropen = pygame.transform.scale(
                imagem_dooropen, (TAMANHO_TILE, TAMANHO_TILE))

            # Desenhar a imagem na célula (x, y)
            screen.blit(imagem_redimensionada_door,
                        (5*TAMANHO_TILE, 32*TAMANHO_TILE))

            screen.blit(imagem_redimensionada_door,
                        (39*TAMANHO_TILE, 17*TAMANHO_TILE))

            screen.blit(imagem_redimensionada_door,
                        (24*TAMANHO_TILE, 1*TAMANHO_TILE))

            if portaaberta == False:
                screen.blit(imagem_redimensionada_door,
                            (6*TAMANHO_TILE, 5*TAMANHO_TILE))
            else:
                screen.blit(imagem_redimensionada_dooropen,
                            (6*TAMANHO_TILE, 5*TAMANHO_TILE))
