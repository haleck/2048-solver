import pygame

pygame.init()

# Всякие там константы
BLOCKS = 4
SIZE_BLOCKS = 110
MARGIN = 10
WIDTH = SIZE_BLOCKS * BLOCKS + MARGIN * (BLOCKS + 1)
HEIGHT = WIDTH + 110

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()


