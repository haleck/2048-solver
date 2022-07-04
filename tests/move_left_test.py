from unittest import TestCase, main
from logic import *


class MoveLeftTest(TestCase):
    def test_move_left_1(self):
        arr = [
            [2, 2, 0, 4],
            [4, 4, 2, 0],
            [8, 2, 4, 0],
            [4, 4, 2, 2]
        ]
        rez = [
            [4, 4, 0, 0],
            [8, 2, 0, 0],
            [8, 2, 4, 0],
            [8, 4, 0, 0]
        ]
        self.assertEqual(move_left(arr), (rez, 24))

    def test_move_left_2(self):
        arr = [
            [2, 2, 2, 2],
            [2, 4, 0, 2],
            [0, 0, 0, 2],
            [2, 0, 4, 4]
        ]
        rez = [
            [4, 4, 0, 0],
            [2, 4, 2, 0],
            [2, 0, 0, 0],
            [2, 8, 0, 0]
        ]
        self.assertEqual(move_left(arr), (rez, 16))

    def test_move_left_3(self):
        arr = [
            [8, 8, 4, 0],
            [2, 0, 2, 4],
            [4, 2, 2, 0],
            [8, 4, 2, 0]
        ]
        rez = [
            [16, 4, 0, 0],
            [4, 4, 0, 0],
            [4, 4, 0, 0],
            [8, 4, 2, 0]
        ]
        self.assertEqual(move_left(arr), (rez, 24))

    def test_move_left_4(self):
        arr = [
            [8, 16, 32, 32],
            [2, 2, 4, 4],
            [2, 8, 8, 2],
            [0, 0, 0, 0]
        ]
        rez = [
            [8, 16, 64, 0],
            [4, 8, 0, 0],
            [2, 16, 2, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_left(arr), (rez, 92))


if __name__ == "__main__":
    main()
