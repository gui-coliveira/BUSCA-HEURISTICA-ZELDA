import pygame
import math
import cria_terreno
import time

# Definir as cores dos diferentes tipos de terreno
GRAMA = (124, 252, 0)
AREIA = (244, 164, 96)
FLORESTA = (34, 139, 34)
MONTANHA = (139, 137, 137)
AGUA = (30, 144, 255)

converte_variavel = {
    "GRAMA": GRAMA,
    "AREIA": AREIA,
    "FLORESTA": FLORESTA,
    "MONTANHA": MONTANHA,
    "AGUA": AGUA
}

# Definir o custo de cada tipo de terrenocl
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
LARGURA_TELA = 800
ALTURA_TELA = 800
TAMANHO_TILE = 19

# Criar a janela
screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Definir as dimensões da matriz do terreno
LINHAS = 42
COLUNAS = 42

# Definir o terreno manualmente

terreno = cria_terreno.retorna_terreno()
terreno_convertido = []
for linha in terreno:
    linha_convertida = []
    for item in linha:
        linha_convertida.append(converte_variavel[item])
    terreno_convertido.append(linha_convertida)

print(terreno)
print(terreno_convertido)
# Adicionar as coordenadas do ponto de partida e destino
ponto_partida = (27, 24)
ponto_destino1 = (32, 5)
ponto_destino2 = (17, 39)
ponto_destino3 = (2, 25)
ponto_espada = (2, 3)


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


def heuristica(celula_atual, ponto_destino1):
    return calcular_distancia(celula_atual.posicao, ponto_destino1) * 10


def custo(celula_atual, vizinho):
    if vizinho in celula_atual.vizinhos:
        return celula_atual.custo + vizinho.custo
    else:
        return float('inf')


def desenhar_caminho(caminho_recente, ponto_start, ponto_dest):
    # Desenhar o ponto de partida
    pygame.draw.rect(screen, (0, 255, 242), (ponto_start[1] *
                                             TAMANHO_TILE, ponto_start[0]*TAMANHO_TILE, TAMANHO_TILE, TAMANHO_TILE))

    # Desenhar o ponto de destino
    pygame.draw.rect(screen, (79, 79, 79), (ponto_dest[1] *
                                            TAMANHO_TILE, ponto_dest[0]*TAMANHO_TILE, TAMANHO_TILE, TAMANHO_TILE))

    pygame.display.update()
    pygame.time.wait(100)

    for celula in caminho_recente:
        x, y = celula
        rect = pygame.Rect(y * TAMANHO_TILE, x * TAMANHO_TILE,
                           TAMANHO_TILE, TAMANHO_TILE)
        pygame.draw.rect(screen, (255, 0, 0), rect)
        pygame.display.update()
        pygame.time.wait(300)


def algoritmo_a_estrela(terreno_convertido, ponto_start, ponto_destino1):
    # Criar as células do terreno
    celulas = [[Celula((linha, coluna), CUSTO[terreno_convertido[linha][coluna]])
                for coluna in range(COLUNAS)] for linha in range(LINHAS)]

    # Conectar as células aos seus vizinhos
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if linha > 0:
                celulas[linha][coluna].vizinhos.append(
                    celulas[linha-1][coluna])
            if linha < LINHAS-1:
                celulas[linha][coluna].vizinhos.append(
                    celulas[linha+1][coluna])
            if coluna > 0:
                celulas[linha][coluna].vizinhos.append(
                    celulas[linha][coluna-1])
            if coluna < COLUNAS-1:
                celulas[linha][coluna].vizinhos.append(
                    celulas[linha][coluna+1])

    # Inicializar as listas aberta e fechada
    aberta = []
    fechada = []

    # Adicionar o ponto de partida à lista aberta
    celula_atual = celulas[ponto_start[0]][ponto_start[1]]
    aberta.append(celula_atual)

    # Loop principal do algoritmo A*
    while aberta:
        # Encontrar a célula na lista aberta com o menor valor de f + h
        celula_atual = min(aberta, key=lambda celula: celula.f + celula.h)

        # Se a célula atual for o ponto de destino, retornar o caminho encontrado
        if celula_atual.posicao == ponto_destino1:
            caminho = []
            custo_total = 0
            while celula_atual:
                caminho.append(celula_atual.posicao)
                celula_atual = celula_atual.pai
                if celula_atual:
                    custo_total+= celula_atual.custo
            return (caminho[::-1], custo_total)

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
            vizinho.h = heuristica(vizinho, ponto_destino1)
            vizinho.f = vizinho.g + vizinho.h
            vizinho.pai = celula_atual

    return None


# Loop principal do jogo
# while True:
# Capturar os eventos do pygame
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

# Desenhar o terreno_convertido na tela
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

destinos = [ponto_destino1, ponto_destino2, ponto_destino3]
menor = 100000000000
indice_destino =0
partida = ponto_partida
caminho_atual = []
while destinos:
    for i, destino_melhor in enumerate(destinos):           
        # Obter o caminho encontrado pelo algoritmo A*
        caminho, custo_total = algoritmo_a_estrela(
            terreno_convertido, partida, destino_melhor)
        if menor > custo_total:
            menor = custo_total
            indice_destino=i
            caminho_atual = caminho
    desenhar_caminho(caminho_atual, partida, destinos[indice_destino])
    # pygame.display.update()
    partida = destinos[indice_destino]
    destinos.remove(destinos[indice_destino])
    menor = 100000000000
    
    

# Desenhar o caminho encontrado
# desenhar_caminho(caminho, ponto_partida, ponto_destino1)

# Atualizar a tela
pygame.display.update()
