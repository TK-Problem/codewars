import unittest


def find_uniq(arr):
    for _ in range(len(arr)-2):
        n = arr.pop()
        if n not in arr:
            return n
    if arr[0] == n:
        return arr[1]
    else:
        return arr[0]


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(2, find_uniq([1, 1, 1, 2, 1, 1]))

    def test_2(self):
        self.assertEqual(10, find_uniq([3, 10, 3, 3, 3]))

    def test_3(self):
        self.assertEqual(0.55, find_uniq([0, 0, 0.55, 0, 0]))

    def test_4(self):
        self.assertEqual(0, find_uniq([0, 1, 1, 1, 1, 1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
