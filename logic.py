import random
from settings import *


def is_there_empty_block(arr: list) -> bool:
    for row in arr:
        if 0 in row:
            return True
    return False


def add_number(arr: list):
    empty_list = []
    for i in range(BLOCKS):
        for j in range(BLOCKS):
            if arr[i][j] == 0:
                empty_list.append((i, j))
    index = random.choice(empty_list)
    arr[index[0]][index[1]] = 2 if random.random() < 0.9 else 4


def move_left(arr: list) -> list:
    for row in arr:
        while 0 in row:
            row.remove(0)
        while len(row) != BLOCKS:
            row.append(0)
    for i in range(BLOCKS):
        for j in range(BLOCKS - 1):
            if arr[i][j] == arr[i][j + 1]:
                arr[i][j] *= 2
                arr[i].pop(j + 1)
                arr[i].append(0)
    return arr


def move_right(arr: list) -> list:
    for row in arr:
        while 0 in row:
            row.remove(0)
        while len(row) != BLOCKS:
            row.insert(0, 0)
    for i in range(BLOCKS):
        for j in range(BLOCKS - 1, 0, -1):
            if arr[i][j] == arr[i][j - 1]:
                arr[i][j] *= 2
                arr[i].pop(j - 1)
                arr[i].insert(0, 0)
    return arr


def rotate_left(arr: list) -> list:
    return [[arr[j][i] for j in range(BLOCKS)] for i in range(BLOCKS)]


def rotate_right(arr: list) -> list:
    for i in range(3):
        arr = rotate_left(arr)
    return arr


def move_up(arr: list) -> list:
    arr = rotate_left(arr)
    arr = move_left(arr)
    arr = rotate_right(arr)
    return arr


def move_down(arr: list) -> list:
    arr = rotate_right(arr)
    arr = move_right(arr)
    arr = rotate_left(arr)
    return arr
