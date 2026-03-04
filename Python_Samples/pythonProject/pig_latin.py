import re
import unittest


def translate(text):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z']
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = text.split()
    flag = False
    result = ""
    for word in words:
        # rule 1
        if word[0:2] == "xr" or word[0:2] == "yt" or word[0] in vowels:
            result = result + word + "ay "
            continue

        # rule 3
        if word[0] in consonants and "qu" in word:
            index = word.find("qu")
            result = result + word[index + 2:] + word[0:index + 2] + "ay "
            continue

        # rule 4
        if word[0] in consonants and word[0] != 'y' and "y" in word:
            index = word.find("y")
            index2 = len(word)
            for i, c in enumerate(word):
                if c in vowels:
                    index2 = i
                    break

            index = min(index, index2)

            result = result + word[index:] + word[0:index] + "ay "
            continue

        # rule 2
        if word[0] in consonants:
            for index, char in enumerate(word):
                if char in vowels:
                    result = result + word[index:] + word[0:index] + "ay "
                    break
            continue

    return result.rstrip()

class PigLatinTest(unittest.TestCase):
    def test_word_beginning_with_a(self):
        self.assertEqual(translate("apple"), "appleay")
    def test_word_beginning_with_e(self):
        self.assertEqual(translate("ear"), "earay")
    def test_word_beginning_with_i(self):
        self.assertEqual(translate("igloo"), "iglooay")
    def test_word_beginning_with_o(self):
        self.assertEqual(translate("object"), "objectay")
    def test_word_beginning_with_u(self):
        self.assertEqual(translate("under"), "underay")
    def test_word_beginning_with_a_vowel_and_followed_by_a_qu(self):
        self.assertEqual(translate("equal"), "equalay")
    def test_word_beginning_with_p(self):
        self.assertEqual(translate("pig"), "igpay")
    def test_word_beginning_with_k(self):
        self.assertEqual(translate("koala"), "oalakay")
    def test_word_beginning_with_x(self):
        self.assertEqual(translate("xenon"), "enonxay")
    def test_word_beginning_with_q_without_a_following_u(self):
        self.assertEqual(translate("qat"), "atqay")
    def test_word_beginning_with_ch(self):
        self.assertEqual(translate("chair"), "airchay")
    def test_word_beginning_with_qu(self):
        self.assertEqual(translate("queen"), "eenquay")
    def test_word_beginning_with_qu_and_a_preceding_consonant(self):
        self.assertEqual(translate("square"), "aresquay")
    def test_word_beginning_with_th(self):
        self.assertEqual(translate("therapy"), "erapythay")
    def test_word_beginning_with_thr(self):
        self.assertEqual(translate("thrush"), "ushthray")
    def test_word_beginning_with_sch(self):
        self.assertEqual(translate("school"), "oolschay")
    def test_word_beginning_with_yt(self):
        self.assertEqual(translate("yttria"), "yttriaay")
    def test_word_beginning_with_xr(self):
        self.assertEqual(translate("xray"), "xrayay")
    def test_y_is_treated_like_a_consonant_at_the_beginning_of_a_word(self):
        self.assertEqual(translate("yellow"), "ellowyay")
    def test_y_is_treated_like_a_vowel_at_the_end_of_a_consonant_cluster(self):
        self.assertEqual(translate("rhythm"), "ythmrhay")
    def test_y_as_second_letter_in_two_letter_word(self):
        self.assertEqual(translate("my"), "ymay")
    def test_a_whole_phrase(self):
        self.assertEqual(translate("quick fast run"), "ickquay astfay unray")

