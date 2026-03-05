import unittest


def resistor_label(colors):
    codes = {"black": 0,
             "brown": 1,
             "red": 2,
             "orange": 3,
             "yellow": 4,
             "green": 5,
             "blue": 6,
             "violet": 7,
             "grey": 8,
             "white": 9}
    resistance = {"ohms", "kiloohms", "megahoms", "gigaohms"}
    tolerance = {"grey": "0.05%",
                 "violet": "0.1%",
                 "blue": "0.25%",
                 "green": "0.5%",
                 "brown": "1%",
                 "red": "2%",
                 "gold": "5%",
                 "silver": "10%"}
    if len(colors) == 4:
        result = codes[colors[0]] * 10 + codes[colors[1]]
        result = result * 10 ** codes[colors[2]]
    elif len(colors) == 5:
        result = codes[colors[0]] * 100 + codes[colors[1]] * 10 + codes[colors[2]]
        result = result * 10 ** codes[colors[3]]
    elif len(colors) == 1:
        return str(codes[colors[0]]) + " ohms"

    if result < 1000:
        result = str(result) + " ohms ±" + tolerance[colors[-1]]
    elif 1_000 <= result < 1_000_000:
        if result % 1_000 == 0:
            result = str(result // 1_000) + " kiloohms ±" + tolerance[colors[-1]]
        else:
            result = str(result / 1_000) + " kiloohms ±" + tolerance[colors[-1]]
    else:
        result = str(result / 1_000_000) + " megaohms ±" + tolerance[colors[-1]]

    return result


class ResistorColorExpertTest(unittest.TestCase):
    def test_orange_orange_black_and_red(self):
        self.assertEqual(resistor_label(["orange", "orange", "black", "red"]), "33 ohms ±2%")

    def test_blue_grey_brown_and_violet(self):
        self.assertEqual(resistor_label(["blue", "grey", "brown", "violet"]), "680 ohms ±0.1%")

    def test_red_black_red_and_green(self):
        self.assertEqual(resistor_label(["red", "black", "red", "green"]), "2 kiloohms ±0.5%")

    def test_green_brown_orange_and_grey(self):
        self.assertEqual(
            resistor_label(["green", "brown", "orange", "grey"]), "51 kiloohms ±0.05%"
        )

    def test_one_black_band(self):
        self.assertEqual(resistor_label(["black"]), "0 ohms")

    def test_orange_orange_yellow_black_and_brown(self):
        self.assertEqual(
            resistor_label(["orange", "orange", "yellow", "black", "brown"]), "334 ohms ±1%"
        )

    def test_red_green_yellow_yellow_and_brown(self):
        self.assertEqual(
            resistor_label(["red", "green", "yellow", "yellow", "brown"]), "2.54 megaohms ±1%"
        )

    def test_blue_grey_white_brown_and_brown(self):
        self.assertEqual(
            resistor_label(["blue", "grey", "white", "brown", "brown"]), "6.89 kiloohms ±1%"
        )

    def test_violet_orange_red_and_grey(self):
        self.assertEqual(
            resistor_label(["violet", "orange", "red", "grey"]), "7.3 kiloohms ±0.05%"
        )

    def test_brown_red_orange_green_and_blue(self):
        self.assertEqual(
            resistor_label(["brown", "red", "orange", "green", "blue"]), "12.3 megaohms ±0.25%"
        )

    def test_brown_black_brown_yellow_and_violet(self):
        self.assertEqual(
            resistor_label(["brown", "black", "brown", "yellow", "violet"]), "1.01 megaohms ±0.1%"
        )

    def test_brown_black_red_and_red(self):
        self.assertEqual(
            resistor_label(["brown", "black", "red", "red"]), "1 kiloohms ±2%"
        )
