# Let's take the ISBN-10 3-598-21508-8. We plug it in to the formula, and get:
#
# (3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0

import re
import unittest


def is_valid(isbn):
    l_number = list(isbn)
    z = re.match(r"^\d-\d{3}-\d{5}-[\dX]$", isbn)
    zz = re.match(r"^\d{9}[\dX]$", isbn)

    if not z and not zz:
        return False

    if len(l_number) == 13:
        del (l_number[11])
        del (l_number[5])
        del (l_number[1])
    print(l_number)
    value = 0
    l_range = [i for i in range(10, 0, -1)]
    for x, y in zip(l_number, l_range):
        if x == 'X':
            x = 10
        value = value + (int(x) * y)
    return value % 11 == 0


class IsbnVerifierTest(unittest.TestCase):
    def test_valid_isbn(self):
        self.assertIs(is_valid("3-598-21508-8"), True)

    def test_invalid_isbn_check_digit(self):
        self.assertIs(is_valid("3-598-21508-9"), False)

    def test_valid_isbn_with_a_check_digit_of_10(self):
        self.assertIs(is_valid("3-598-21507-X"), True)

    def test_check_digit_is_a_character_other_than_x(self):
        self.assertIs(is_valid("3-598-21507-A"), False)

    def test_invalid_check_digit_in_isbn_is_not_treated_as_zero(self):
        self.assertIs(is_valid("4-598-21507-B"), False)

    def test_invalid_character_in_isbn_is_not_treated_as_zero(self):
        self.assertIs(is_valid("3-598-P1581-X"), False)

    def test_x_is_only_valid_as_a_check_digit(self):
        self.assertIs(is_valid("3-598-2X507-9"), False)

    def test_only_one_check_digit_is_allowed(self):
        self.assertIs(is_valid("3-598-21508-96"), False)

    def test_x_is_not_substituted_by_the_value_10(self):
        self.assertIs(is_valid("3-598-2X507-5"), False)

    def test_valid_isbn_without_separating_dashes(self):
        self.assertIs(is_valid("3598215088"), True)

    def test_isbn_without_separating_dashes_and_x_as_check_digit(self):
        self.assertIs(is_valid("359821507X"), True)

    def test_isbn_without_check_digit_and_dashes(self):
        self.assertIs(is_valid("359821507"), False)

    def test_too_long_isbn_and_no_dashes(self):
        self.assertIs(is_valid("3598215078X"), False)

    def test_too_short_isbn(self):
        self.assertIs(is_valid("00"), False)

    def test_isbn_without_check_digit(self):
        self.assertIs(is_valid("3-598-21507"), False)

    def test_check_digit_of_x_should_not_be_used_for_0(self):
        self.assertIs(is_valid("3-598-21515-X"), False)

    def test_empty_isbn(self):
        self.assertIs(is_valid(""), False)

    def test_input_is_9_characters(self):
        self.assertIs(is_valid("134456729"), False)

    def test_invalid_characters_are_not_ignored_after_checking_length(self):
        self.assertIs(is_valid("3132P34035"), False)

    def test_invalid_characters_are_not_ignored_before_checking_length(self):
        self.assertIs(is_valid("3598P215088"), False)

    def test_input_is_too_long_but_contains_a_valid_isbn(self):
        self.assertIs(is_valid("98245726788"), False)
