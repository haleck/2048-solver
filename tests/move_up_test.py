from unittest import TestCase, main
from logic import *


class MoveUpTest(TestCase):
    def test_move_up_1(self):
        arr = [
            [2, 2, 2, 0],
            [0, 0, 4, 2],
            [0, 2, 2, 0],
            [2, 0, 0, 0]
        ]
        rez = [
            [4, 4, 2, 2],
            [0, 0, 4, 0],
            [0, 0, 2, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(arr), (rez, 8))

    def test_move_up_2(self):
        arr = [
            [2, 2, 0, 2],
            [2, 4, 0, 0],
            [2, 4, 2, 2],
            [2, 2, 0, 2]
        ]
        rez = [
            [4, 2, 2, 4],
            [4, 8, 0, 2],
            [0, 2, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(arr), (rez, 20))

    def test_move_up_3(self):
        arr = [
            [4, 2, 4, 2],
            [2, 0, 8, 0],
            [0, 2, 8, 0],
            [2, 2, 8, 2]
        ]
        rez = [
            [4, 4, 4, 4],
            [4, 2, 16, 0],
            [0, 0, 8, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(arr), (rez, 28))

    def test_move_up_4(self):
        arr = [
            [2, 4, 2, 4],
            [2, 0, 2, 8],
            [2, 4, 2, 0],
            [0, 4, 0, 8]
        ]
        rez = [
            [4, 8, 4, 4],
            [2, 4, 2, 16],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(arr), (rez, 32))

    def test_move_up_5(self):
        arr = [
            [0, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 2, 0],
            [0, 4, 0, 8]
        ]
        rez = [
            [0, 2, 2, 8],
            [0, 4, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(arr), (rez, 0))


if __name__ == "__main__":
    main()
