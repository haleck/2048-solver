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
empty_arr = [arr[i].copy() for i in range(len(arr))]


def draw_blocks(array: list, i_range=range(BLOCKS), j_range=range(BLOCKS)):
    for i in i_range:
        for j in j_range:
            number = array[i][j]
            start_x = MARGIN * (j + 1) + SIZE_BLOCKS * j
            start_y = MARGIN * (i + 1) + SIZE_BLOCKS * i + SIZE_BLOCKS
            block = pygame.Rect(start_x, start_y, SIZE_BLOCKS, SIZE_BLOCKS)
            pygame.draw.rect(screen, COLORS[number][0], block)
            if number:
                text = numbers_font.render(f"{number}", True, COLORS[number][1])
                text_rect = text.get_rect(center=(start_x + SIZE_BLOCKS / 2, start_y + SIZE_BLOCKS / 2))
                screen.blit(text, text_rect)


def write_record(record):
    with open("record.txt", "w") as f:
        f.write(record)


def read_record() -> int:
    with open("record.txt", "r") as f:
        try:
            record = int(f.read())
            return record
        except ValueError:
            return -1


def draw_header(score):
    pygame.draw.rect(screen, HEADER_COLOR, header)

    text_score = score_font.render(f"{score}", True, TEXT_COLOR_DARK)
    screen.blit(text_score, (20, 10))

    record = read_record()
    text_record = record_font.render(f"{record if record > score else score}", True, LIGHT_COLOR)
    text_record_label = record_label_font.render(f"BEST", True, TEXT_COLOR)
    width_record_text = 120 if text_record.get_width() < 120 else text_record.get_width() + 20
    height_record_text = 60
    block = pygame.Rect((
        WIDTH - width_record_text - MARGIN, SIZE_BLOCKS / 2 - height_record_text / 2, width_record_text,
        height_record_text))
    pygame.draw.rect(screen, MAIN_COLOR, block)
    screen.blit(text_record,
                (WIDTH - width_record_text / 2 - MARGIN - text_record.get_width() / 2, height_record_text / 2 + 18))
    screen.blit(text_record_label, (
        WIDTH - width_record_text / 2 - MARGIN - text_record_label.get_width() / 2, height_record_text / 2 + 3))


score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            last_arr = [arr[i].copy() for i in range(len(arr))]
            delta = 0
            if event.key == pygame.K_LEFT:
                arr, delta = move_left(arr)
            elif event.key == pygame.K_UP:
                arr, delta = move_up(arr)
            elif event.key == pygame.K_RIGHT:
                arr, delta = move_right(arr)
            elif event.key == pygame.K_DOWN:
                arr, delta = move_down(arr)
            if arr != last_arr:
                add_number(arr)
            elif arr == empty_arr:
                add_number(arr)
            score += delta

    screen.fill(MAIN_COLOR)
    draw_header(score)

    draw_blocks(arr)

    pygame.display.update()
