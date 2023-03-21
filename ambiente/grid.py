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

VERMELHO = (255, 0, 0)

# Inicializar o pygame
pygame.init()

# Definir as dimensões da tela e o tamanho dos tiles
LARGURA_TELA = 940
ALTURA_TELA = 1280
TAMANHO_TILE = 50

# Criar a janela
screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Definir as dimensões da matriz do terreno
LINHAS = 10
COLUNAS = 10

# Definir o terreno manualmente

terreno = [    [FLORESTA, FLORESTA, FLORESTA, FLORESTA, FLORESTA, FLORESTA, FLORESTA, FLORESTA, FLORESTA, FLORESTA],
    [FLORESTA, GRAMA, GRAMA, FLORESTA, GRAMA, FLORESTA, GRAMA, FLORESTA, GRAMA, GRAMA],
    [FLORESTA, GRAMA, FLORESTA, FLORESTA, AGUA, GRAMA, AREIA, FLORESTA, FLORESTA, AGUA],
    [FLORESTA, GRAMA, MONTANHA, FLORESTA, AGUA, GRAMA, GRAMA, MONTANHA, FLORESTA, AGUA],
    [FLORESTA, GRAMA, MONTANHA, GRAMA, GRAMA, MONTANHA, MONTANHA, MONTANHA, GRAMA, GRAMA],
    [FLORESTA, GRAMA, GRAMA, AGUA, AGUA, GRAMA, GRAMA, GRAMA, AGUA, AGUA],
    [FLORESTA, GRAMA, GRAMA, AGUA, AGUA, GRAMA, AREIA, GRAMA, AGUA, AGUA],
    [FLORESTA, GRAMA, FLORESTA, FLORESTA, AGUA, GRAMA, AREIA, FLORESTA, FLORESTA, AGUA],
    [FLORESTA, FLORESTA, MONTANHA, FLORESTA, AGUA, GRAMA, GRAMA, MONTANHA, FLORESTA, AGUA],
    [FLORESTA, GRAMA, MONTANHA, GRAMA, GRAMA, MONTANHA, MONTANHA, MONTANHA, GRAMA, GRAMA]
]


# Adicionar as coordenadas do ponto de partida e destino
ponto_partida = (0, 0)
ponto_destino = (9, 9)
#inicial = (25, 28) dungeon1 = (6, 33) dungeon2 = (40, 18) dungeon3 = (25, 2) porta = (7, 6) espada = (3, 2)


def calcular_distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class Celula:
    def __init__(self, posicao, custo):
        self.posicao = posicao
        self.custo = custo
        self.vizinhos = []
        self.g = 0
        self.h = 0
        self.f = 0
        self.pai = None
        self.visitada = False

    def reset(self):
        self.g = 0
        self.h = 0
        self.f = 0
        self.pai = None
        self.visitada = False


def heuristica(celula_atual, ponto_destino):
    return calcular_distancia(celula_atual.posicao, ponto_destino) * 10

def custo(celula_atual, vizinho):
    if vizinho in celula_atual.vizinhos:
        return celula_atual.custo + vizinho.custo
    else:
        return float('inf')

def algoritmo_a_estrela(terreno, ponto_partida, ponto_destino):
    # Criar as células do terreno
    celulas = [[Celula((linha, coluna), CUSTO[terreno[linha][coluna]]) for coluna in range(COLUNAS)] for linha in range(LINHAS)]

    # Conectar as células aos seus vizinhos
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if linha > 0:
                celulas[linha][coluna].vizinhos.append(celulas[linha-1][coluna])
            if linha < LINHAS-1:
                celulas[linha][coluna].vizinhos.append(celulas[linha+1][coluna])
            if coluna > 0:
                celulas[linha][coluna].vizinhos.append(celulas[linha][coluna-1])
            if coluna < COLUNAS-1:
                celulas[linha][coluna].vizinhos.append(celulas[linha][coluna+1])

    # Inicializar as listas aberta e fechada
    aberta = []
    fechada = []

    # Adicionar o ponto de partida à lista aberta
    celula_atual = celulas[ponto_partida[0]][ponto_partida[1]]
    aberta.append(celula_atual)

    # Loop principal do algoritmo A*
    while aberta:
        # Encontrar a célula na lista aberta com o menor valor de f + h
        celula_atual = min(aberta, key=lambda celula: celula.f + celula.h)

        # Se a célula atual for o ponto de destino, retornar o caminho encontrado
        if celula_atual.posicao == ponto_destino:
            caminho = []
            while celula_atual:
                caminho.append(celula_atual.posicao)
                celula_atual = celula_atual.pai
            return caminho[::-1]

        # Remover a célula atual da lista aberta e adicioná-la à lista fechada
        aberta.remove(celula_atual)
        fechada.append(celula_atual)

        # Verificar todos os vizinhos da célula atual
        for vizinho in celula_atual.vizinhos:
            # Se o vizinho estiver na lista fechada, ignorá-lo
            if vizinho in fechada:
                continue

            # Calcular o custo do caminho da célula atual até o vizinho
            novo_g = celula_atual.g + custo(celula_atual, vizinho)

            # Se o vizinho não estiver na lista aberta, adicioná-lo
            if vizinho not in aberta:
                aberta.append(vizinho)
            # Se o novo caminho para o vizinho for mais longo do que o já calculado, ignorá-lo
            elif novo_g >= vizinho.g:
                continue

            # Atualizar os valores de g, h e f do vizinho
            vizinho.g = novo_g
            vizinho.h = heuristica(vizinho, ponto_destino)
            vizinho.f = vizinho.g + vizinho.h
            vizinho.pai = celula_atual

    # Encontrar o caminho mais curto
    caminho = []
    celula_atual = celulas[ponto_destino[0]][ponto_destino[1]]
    while celula_atual.pai is not None:
        caminho.append(celula_atual.posicao)
        celula_atual = celula_atual.pai
    caminho.append(ponto_partida)
    

    # Pintar o caminho mais curto de vermelho
    for posicao in caminho:
        x, y = posicao
        pygame.draw.rect(screen, VERMELHO, (y*TAMANHO_TILE, x*TAMANHO_TILE, TAMANHO_TILE, TAMANHO_TILE))

    # Se não houver caminho para o ponto de destino, retornar None
    return None
          


# Loop principal do jogo
while True:
    print(algoritmo_a_estrela(terreno, ponto_partida, ponto_destino))
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
if encontrou_destino:
    # Pintar o caminho mais curto de vermelho
    celula_atual = celula_destino
    while celula_atual.pai is not None:
        celula_atual = celula_atual.pai
        x, y = celula_atual.posicao
        pygame.draw.rect(screen, VERMELHO, (y * TAMANHO_TILE, x * TAMANHO_TILE, TAMANHO_TILE, TAMANHO_TILE))
  