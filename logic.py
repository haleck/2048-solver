import random
from settings import *


def is_there_empty_block(arr: list) -> bool:
    for row in arr:
        if 0 in row:
            return True
    return False


def add_number(arr: list) -> None:
    empty_list = []
    for i in range(BLOCKS):
        for j in range(BLOCKS):
            if arr[i][j] == 0:
                empty_list.append((i, j))
    index = random.choice(empty_list)
    arr[index[0]][index[1]] = 2 if random.random() < 0.9 else 4


def move_left(arr: list) -> tuple:
    delta = 0
    for row in arr:
        while 0 in row:
            row.remove(0)
        while len(row) != BLOCKS:
            row.append(0)
    for i in range(BLOCKS):
        for j in range(BLOCKS - 1):
            if arr[i][j] == arr[i][j + 1]:
                arr[i][j] *= 2
                delta += arr[i][j]
                arr[i].pop(j + 1)
                arr[i].append(0)
    return arr, delta


def move_right(arr: list) -> tuple:
    delta = 0
    for row in arr:
        while 0 in row:
            row.remove(0)
        while len(row) != BLOCKS:
            row.insert(0, 0)
    for i in range(BLOCKS):
        for j in range(BLOCKS - 1, 0, -1):
            if arr[i][j] == arr[i][j - 1]:
                arr[i][j] *= 2
                delta += arr[i][j]
                arr[i].pop(j - 1)
                arr[i].insert(0, 0)
    return arr, delta


def transpose(arr: list) -> list:
    return [[arr[j][i] for j in range(BLOCKS)] for i in range(BLOCKS)]


def move_up(arr: list) -> tuple:
    arr = transpose(arr)
    arr, delta = move_left(arr)
    arr = transpose(arr)
    return arr, delta


def move_down(arr: list) -> tuple:
    arr = transpose(arr)
    arr, delta = move_right(arr)
    arr = transpose(arr)
    return arr, delta
