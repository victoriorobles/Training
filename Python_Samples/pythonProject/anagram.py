import string
import unittest


def find_anagrams(word, candidates):
    w1 = convert_dict(word.lower())
    result = []
    for w in candidates:
        w2 = convert_dict(w.lower())
        if word.lower() == w.lower():
            continue
        if w1 == w2:
            result.append(w)
    return result


def convert_dict(word1):
    d = dict()
    word2 = ''.join(sorted(word1))
    d = {char: word2.count(char) for char in set(word2)}

    return d

# def detect_anagrams(word, wordlist):
#     return [w for w in wordlist if sorted(word.lower()) == sorted(w.lower())\
#                                      and word.lower() != w.lower()]

class AnagramTest(unittest.TestCase):
    def test_no_matches(self):
        candidates = ["hello", "world", "zombies", "pants"]
        expected = []
        self.assertCountEqual(find_anagrams("diaper", candidates), expected)

    def test_detects_two_anagrams(self):
        candidates = ["lemons", "cherry", "melons"]
        expected = ["lemons", "melons"]
        self.assertCountEqual(find_anagrams("solemn", candidates), expected)

    def test_does_not_detect_anagram_subsets(self):
        candidates = ["dog", "goody"]
        expected = []
        self.assertCountEqual(find_anagrams("good", candidates), expected)

    def test_detects_anagram(self):
        candidates = ["enlists", "google", "inlets", "banana"]
        expected = ["inlets"]
        self.assertCountEqual(find_anagrams("listen", candidates), expected)

    def test_detects_three_anagrams(self):
        candidates = ["gallery", "ballerina", "regally", "clergy", "largely", "leading"]
        expected = ["gallery", "regally", "largely"]
        self.assertCountEqual(find_anagrams("allergy", candidates), expected)

    def test_detects_multiple_anagrams_with_different_case(self):
        candidates = ["Eons", "ONES"]
        expected = ["Eons", "ONES"]
        self.assertCountEqual(find_anagrams("nose", candidates), expected)

    def test_does_not_detect_non_anagrams_with_identical_checksum(self):
        candidates = ["last"]
        expected = []
        self.assertCountEqual(find_anagrams("mass", candidates), expected)

    def test_detects_anagrams_case_insensitively(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        expected = ["Carthorse"]
        self.assertCountEqual(find_anagrams("Orchestra", candidates), expected)

    def test_detects_anagrams_using_case_insensitive_subject(self):
        candidates = ["cashregister", "carthorse", "radishes"]
        expected = ["carthorse"]
        self.assertCountEqual(find_anagrams("Orchestra", candidates), expected)

    def test_detects_anagrams_using_case_insensitive_possible_matches(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        expected = ["Carthorse"]
        self.assertCountEqual(find_anagrams("orchestra", candidates), expected)

    def test_does_not_detect_an_anagram_if_the_original_word_is_repeated(self):
        candidates = ["goGoGO"]
        expected = []
        self.assertCountEqual(find_anagrams("go", candidates), expected)

    def test_anagrams_must_use_all_letters_exactly_once(self):
        candidates = ["patter"]
        expected = []
        self.assertCountEqual(find_anagrams("tapper", candidates), expected)

    def test_words_are_not_anagrams_of_themselves(self):
        candidates = ["BANANA"]
        expected = []
        self.assertCountEqual(find_anagrams("BANANA", candidates), expected)

    def test_words_are_not_anagrams_of_themselves_even_if_letter_case_is_partially_different(
            self,
    ):
        candidates = ["Banana"]
        expected = []
        self.assertCountEqual(find_anagrams("BANANA", candidates), expected)

    def test_words_are_not_anagrams_of_themselves_even_if_letter_case_is_completely_different(
            self,
    ):
        candidates = ["banana"]
        expected = []
        self.assertCountEqual(find_anagrams("BANANA", candidates), expected)

    def test_words_other_than_themselves_can_be_anagrams(self):
        candidates = ["LISTEN", "Silent"]
        expected = ["Silent"]
        self.assertCountEqual(find_anagrams("LISTEN", candidates), expected)

    def test_handles_case_of_greek_letters(self):
        candidates = ["ΒΓΑ", "ΒΓΔ", "γβα", "αβγ"]
        expected = ["ΒΓΑ", "γβα"]
        self.assertCountEqual(find_anagrams("ΑΒΓ", candidates), expected)

    def test_different_characters_may_have_the_same_bytes(self):
        candidates = ["€a"]
        expected = []
        self.assertCountEqual(find_anagrams("a⬂", candidates), expected)
