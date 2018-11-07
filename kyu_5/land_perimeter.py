import unittest
from itertools import cycle


def land_perimeter(arr):
    total_walls = 0
    # calculate side walls
    for row in arr:
        s_walls = 0
        target = cycle(["O", "X"])
        t = next(target)
        for pos in range(len(row)):
            if row[pos] != t:
                s_walls += 1
                t = next(target)

            if pos == len(row)-1 and row[pos] == "X":
                s_walls += 1

        total_walls += s_walls
    # calculate top/bottom walls
    arr_t = ["".join([arr[y][x] for y in range(len(arr))]) for x in range(len(arr[0]))]

    for row in arr_t:
        s_walls = 0
        target = cycle(["O", "X"])
        t = next(target)
        for pos in range(len(row)):
            if row[pos] != t:
                s_walls += 1
                t = next(target)

            if pos == len(row)-1 and row[pos] == "X":
                s_walls += 1
        total_walls += s_walls
    return "Total land perimeter: {}".format(total_walls)


# Testsing
class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX",
                                         "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]),
                         "Total land perimeter: 60")

    def test_2(self):
        self.assertEqual(land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO",
                                         "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]),
                         "Total land perimeter: 52")

    def test_3(self):
        self.assertEqual(land_perimeter(["XXXXXOOO",
                                         "OOXOOOOO",
                                         "OOOOOOXO",
                                         "XXXOOOXO",
                                         "OXOXXOOX"]),
                         "Total land perimeter: 40")

    def test_4(self):
        self.assertEqual(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO",
                                         "OOOOOXX", "OOOXOXX", "XXXXOXO"]),
                         "Total land perimeter: 54")

    def test_5(self):
        self.assertEqual(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO",
                                         "OOOOOO", "OOOXOO", "OOXXOO"]),
                         "Total land perimeter: 40")


if __name__ == '__main__':
    unittest.main()

