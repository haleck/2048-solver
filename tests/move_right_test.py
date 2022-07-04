from unittest import TestCase, main
from logic import *


class MoveRightTest(TestCase):
    def test_move_right_1(self):
        arr = [
            [2, 0, 0, 0],
            [0, 4, 2, 0],
            [0, 2, 2, 2],
            [2, 4, 2, 0]
        ]
        rez = [
            [0, 0, 0, 2],
            [0, 0, 4, 2],
            [0, 0, 2, 4],
            [0, 2, 4, 2]
        ]
        self.assertEqual(move_right(arr), (rez, 4))

    def test_move_right_2(self):
        arr = [
            [0, 2, 0, 2],
            [4, 0, 4, 0],
            [4, 0, 0, 2],
            [0, 2, 0, 0]
        ]
        rez = [
            [0, 0, 0, 4],
            [0, 0, 0, 8],
            [0, 0, 4, 2],
            [0, 0, 0, 2]
        ]
        self.assertEqual(move_right(arr), (rez, 12))

    def test_move_right_3(self):
        arr = [
            [4, 0, 0, 8],
            [0, 2, 4, 0],
            [2, 2, 2, 2],
            [0, 4, 0, 4]
        ]
        rez = [
            [0, 0, 4, 8],
            [0, 0, 2, 4],
            [0, 0, 4, 4],
            [0, 0, 0, 8]
        ]
        self.assertEqual(move_right(arr), (rez, 16))

    def test_move_right_4(self):
        arr = [
            [2, 2, 4, 4],
            [2, 8, 4, 0],
            [8, 2, 2, 4],
            [0, 0, 2, 0]
        ]
        rez = [
            [0, 0, 4, 8],
            [0, 2, 8, 4],
            [0, 8, 4, 4],
            [0, 0, 0, 2]
        ]
        self.assertEqual(move_right(arr), (rez, 16))


if __name__ == "__main__":
    main()
