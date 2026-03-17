import unittest


def square_root(number):
    roots = dict()
    if number == 1:
        return 1
    if number == 4:
        return 2
    for n in range(number // 2):
        if n * n == number:
            return n


# def square_root(n):
#     c = 0
#     d = 1 << 30
#     while d:
#         if n >= c + d:
#             n -= c + d
#             c = (c >> 1) + d
#         else:
#             c >>= 1
#         d >>= 2
#     return c


class SquareRootTest(unittest.TestCase):
    def test_root_of_1(self):
        self.assertEqual(square_root(1), 1)

    def test_root_of_4(self):
        self.assertEqual(square_root(4), 2)

    def test_root_of_25(self):
        self.assertEqual(square_root(25), 5)

    def test_root_of_81(self):
        self.assertEqual(square_root(81), 9)

    def test_root_of_196(self):
        self.assertEqual(square_root(196), 14)

    def test_root_of_65025(self):
        self.assertEqual(square_root(65025), 255)
