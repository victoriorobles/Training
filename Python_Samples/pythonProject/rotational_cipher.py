import unittest


def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_cap = alphabet.upper()
    alp_list = list(alphabet)
    rot = alphabet[key:len(alphabet)] + alphabet[0:key]
    rot_cap = alphabet_cap[key:len(alphabet_cap)] + alphabet_cap[0:key]

    alp_dict = dict(zip(alphabet, rot))
    alp_dict_cap = dict(zip(alphabet_cap, rot_cap))
    result = list()
    for a1 in text:
        if a1 in alp_dict:
            result.append(alp_dict[a1])
        elif a1 in alp_dict_cap:
            result.append(alp_dict_cap[a1])
        else:
            result.append(a1)

    return ("".join(result))
    # return alphabet_cap
    pass


class RotationalCipherTest(unittest.TestCase):
    def test_rotate_a_by_0_same_output_as_input(self):
        self.assertEqual(rotate("a", 0), "a")

    def test_rotate_a_by_1(self):
        self.assertEqual(rotate("a", 1), "b")

    def test_rotate_a_by_26_same_output_as_input(self):
        self.assertEqual(rotate("a", 26), "a")

    def test_rotate_m_by_13(self):
        self.assertEqual(rotate("m", 13), "z")

    def test_rotate_n_by_13_with_wrap_around_alphabet(self):
        self.assertEqual(rotate("n", 13), "a")

    def test_rotate_capital_letters(self):
        self.assertEqual(rotate("OMG", 5), "TRL")

    def test_rotate_spaces(self):
        self.assertEqual(rotate("O M G", 5), "T R L")

    def test_rotate_numbers(self):
        self.assertEqual(rotate("Testing 1 2 3 testing", 4), "Xiwxmrk 1 2 3 xiwxmrk")

    def test_rotate_punctuation(self):
        self.assertEqual(rotate("Let's eat, Grandma!", 21), "Gzo'n zvo, Bmviyhv!")

    def test_rotate_all_letters(self):
        self.assertEqual(
            rotate("The quick brown fox jumps over the lazy dog.", 13),
            "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.",
        )
