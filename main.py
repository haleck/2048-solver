import pygame
from settings import *
from logic import *

# Pygame constants
pygame.init()
pygame.display.set_caption("2048")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
header = pygame.Rect(0, 0, WIDTH, SIZE_BLOCKS)
clock = pygame.time.Clock()

# Pygame fonts
numbers_font = pygame.font.SysFont(MAIN_FONT, 32)
score_font = pygame.font.SysFont(MAIN_FONT, 64)
record_font = pygame.font.SysFont(MAIN_FONT, 24)
record_label_font = pygame.font.SysFont("roboto", 26)

arr = [[0] * BLOCKS for i in range(BLOCKS)]
arr = [[2, 4, 8, 0], [16, 32, 64, 128], [0, 2, 8, 16], [512, 0, 2, 8]]
print(arr)


def draw_block(i, j, color, text_color, number):
    start_x = MARGIN * (i + 1) + SIZE_BLOCKS * i
    start_y = MARGIN * (j + 1) + SIZE_BLOCKS * j + SIZE_BLOCKS
    block = pygame.Rect(start_x, start_y, SIZE_BLOCKS, SIZE_BLOCKS)
    pygame.draw.rect(screen, color, block)
    if number:
        text = numbers_font.render(f"{number}", True, text_color)
        text_rect = text.get_rect(center=(start_x + SIZE_BLOCKS / 2, start_y + SIZE_BLOCKS / 2))
        screen.blit(text, text_rect)


def read_record():
    with open("record.txt", "r") as f:
        try:
            record = int(f.read())
            return record
        except ValueError:
            return "Error"


def draw_header():
    pygame.draw.rect(screen, HEADER_COLOR, header)

    text_score = score_font.render(f"{sum([j for i in arr for j in i])}", True, TEXT_COLOR_DARK)
    screen.blit(text_score, (20, 10))

    record = read_record()
    text_record = record_font.render(f"{record}", True, LIGHT_COLOR)
    text_record_label = record_label_font.render(f"BEST", True, TEXT_COLOR)
    width_record_text = 120 if text_record.get_width() < 120 else text_record.get_width() + 20
    height_record_text = 60
    block = pygame.Rect((WIDTH - width_record_text - MARGIN, SIZE_BLOCKS / 2 - height_record_text / 2, width_record_text, height_record_text))
    pygame.draw.rect(screen, MAIN_COLOR, block)
    screen.blit(text_record, (WIDTH - width_record_text / 2 - MARGIN - text_record.get_width() / 2, height_record_text / 2 + 18))
    screen.blit(text_record_label, (WIDTH - width_record_text / 2 - MARGIN - text_record_label.get_width() / 2, height_record_text / 2 + 3))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(MAIN_COLOR)
    draw_header()

    # Creating game field
    for i in range(BLOCKS):
        for j in range(BLOCKS):
            if arr[i][j] == 0:
                draw_block(i, j, BLOCK_COLOR_0, DARK_COLOR, 0)
            elif arr[i][j] == 2:
                draw_block(i, j, BLOCK_COLOR_2, DARK_COLOR, 2)
            elif arr[i][j] == 4:
                draw_block(i, j, BLOCK_COLOR_4, LIGHT_COLOR, 4)
            elif arr[i][j] == 8:
                draw_block(i, j, BLOCK_COLOR_8, LIGHT_COLOR, 8)
            elif arr[i][j] == 16:
                draw_block(i, j, BLOCK_COLOR_16, LIGHT_COLOR, 16)
            elif arr[i][j] == 32:
                draw_block(i, j, BLOCK_COLOR_32, LIGHT_COLOR, 32)
            elif arr[i][j] == 64:
                draw_block(i, j, BLOCK_COLOR_64, LIGHT_COLOR, 64)
            elif arr[i][j] == 128:
                draw_block(i, j, BLOCK_COLOR_128, LIGHT_COLOR, 128)
            else:
                draw_block(i, j, BLOCK_COLOR_512, LIGHT_COLOR, arr[i][j])

    pygame.display.update()
