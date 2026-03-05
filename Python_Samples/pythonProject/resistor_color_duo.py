import unittest


def value(colors):
    color = {"black": 0,
             "brown": 1,
             "red": 2,
             "orange": 3,
             "yellow": 4,
             "green": 5,
             "blue": 6,
             "violet": 7,
             "grey": 8,
             "white": 9}
    result = color[colors[0]] * 10 + color[colors[1]]
    return result


class ResistorColorDuoTest(unittest.TestCase):
    def test_brown_and_black(self):
        self.assertEqual(value(["brown", "black"]), 10)

    def test_blue_and_grey(self):
        self.assertEqual(value(["blue", "grey"]), 68)

    def test_yellow_and_violet(self):
        self.assertEqual(value(["yellow", "violet"]), 47)

    def test_white_and_red(self):
        self.assertEqual(value(["white", "red"]), 92)

    def test_orange_and_orange(self):
        self.assertEqual(value(["orange", "orange"]), 33)

    def test_ignore_additional_colors(self):
        self.assertEqual(value(["green", "brown", "orange"]), 51)

    def test_black_and_brown_one_digit(self):
        self.assertEqual(value(["black", "brown"]), 1)
