import pygame

pygame.init()

screen_width = 940
screen_height = 1280
screen = pygame.display.set_mode((screen_width, screen_height))


tile_size = 22
rows = 42
cols = 42

item_row = 20
item_col = 0


while True:
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(screen, (34,139,34), (col*tile_size, row*tile_size, tile_size, tile_size), 1)

            if row == item_row and col == item_col:
                pygame.draw.circle(screen, (255, 255, 255), (col*tile_size + tile_size//2, row*tile_size + tile_size//2), tile_size//2)
    
    
    pygame.display.update()

# grid = {}
# for row in range(rows):
#     for col in range(cols):
#         grid[(row, col)] = {
#             'cost': 1,  # custo de movimento da célula
#             'distance': None,  # distância estimada para o objetivo
#             'visited': False,  # indica se a célula foi visitada ou não
#             'parent': None  # célula pai para reconstruir o caminho
#         }
