from unittest import TestCase, main
from logic import *


class MoveDownTest(TestCase):
    def test_move_down_1(self):
        arr = [
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        rez = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 0, 0]
        ]
        self.assertEqual(move_down(arr), rez)

    def test_move_down_2(self):
        arr = [
            [2, 4, 2, 0],
            [2, 0, 4, 2],
            [2, 2, 0, 0],
            [2, 2, 4, 0]
        ]
        rez = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 4, 2, 0],
            [4, 4, 8, 2]
        ]
        self.assertEqual(move_down(arr), rez)

    def test_move_down_3(self):
        arr = [
            [0, 4, 0, 0],
            [2, 0, 2, 2],
            [2, 4, 2, 2],
            [4, 0, 2, 0]
        ]
        rez = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 2, 0],
            [4, 8, 4, 4]
        ]
        self.assertEqual(move_down(arr), rez)

    def test_move_down_4(self):
        arr = [
            [0, 4, 0, 2],
            [0, 4, 2, 0],
            [2, 0, 2, 0],
            [2, 2, 0, 4]
        ]
        rez = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 8, 0, 2],
            [4, 2, 4, 4]
        ]
        self.assertEqual(move_down(arr), rez)


if __name__ == "__main__":
    main()
