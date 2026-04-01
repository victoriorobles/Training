import unittest


def commands(binary_str):
    dictionary = {1: "wink", 2 : "double blink", 4: "close your eyes", 8: "jump",
        16: "Reverse the order of the operations in the secret" }
    lista = []
    number = int(binary_str, 2)
    div = 1
    flag = False
    while div < 31:
        if number & div:
            if not flag:
                lista.append(dictionary[div])
            else:
                lista.reverse()
            number -= div
        div = div * 2
        if div == 16:
            flag = True
    return lista


class SecretHandshakeTest(unittest.TestCase):
    def test_wink_for_1(self):
        self.assertEqual(commands("00001"), ["wink"])

    def test_double_blink_for_10(self):
        self.assertEqual(commands("00010"), ["double blink"])

    def test_close_your_eyes_for_100(self):
        self.assertEqual(commands("00100"), ["close your eyes"])

    def test_jump_for_1000(self):
        self.assertEqual(commands("01000"), ["jump"])

    def test_combine_two_actions(self):
        self.assertEqual(commands("00011"), ["wink", "double blink"])

    def test_reverse_two_actions(self):
        self.assertEqual(commands("10011"), ["double blink", "wink"])

    def test_reversing_one_action_gives_the_same_action(self):
        self.assertEqual(commands("11000"), ["jump"])

    def test_reversing_no_actions_still_gives_no_actions(self):
        self.assertEqual(commands("10000"), [])

    def test_all_possible_actions(self):
        self.assertEqual(
            commands("01111"), ["wink", "double blink", "close your eyes", "jump"]
        )

    def test_reverse_all_possible_actions(self):
        self.assertEqual(
            commands("11111"), ["jump", "close your eyes", "double blink", "wink"]
        )

    def test_do_nothing_for_zero(self):
        self.assertEqual(commands("00000"), [])
