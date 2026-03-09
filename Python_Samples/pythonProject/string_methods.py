"""Functions to help edit essay homework using string manipulation."""
import unittest


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """
    l_list = title.split(" ")
    result = ""
    for item in l_list:
        # one form
        # result = result + " " + item[0].upper() + item[1:]
        # second form
        result = result + " " + item.capitalize()
    result = result.strip()
    # easy way
    # result = title.title()
    return result


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """
    result = sentence[-1] == "."
    return result


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """
    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """
    if old_word in sentence:
        result = sentence.replace(old_word, new_word)
    return result


class StringMethodsTest(unittest.TestCase):
    def test_capitalize_title(self):
        actual_result = capitalize_title("fish are cold blooded")
        expected = "Fish Are Cold Blooded"
        error_message = (f'Called capitalize_title("fish are cold blooded"). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" for the title.')

        self.assertEqual(actual_result, expected, msg=error_message)

    def test_sentence_without_period(self):
        actual_result = check_sentence_ending("Fittonia are nice")
        expected = False
        error_message = (f'Called check_sentence_ending("Fittonia are nice"). '
                         f'The function returned {actual_result}, '
                         f'but the tests expected {expected} for a period ending.')

        self.assertEqual(actual_result, expected, msg=error_message)

    def test_sentence_with_period(self):
        actual_result = check_sentence_ending("Snails can sleep for 3 years.")
        expected = True
        error_message = (f'Called check_sentence_ending("Snails can sleep for 3 years."). '
                         f'The function returned {actual_result}, '
                         f'but the tests expected {expected} for a period ending.')

        self.assertEqual(actual_result, expected, msg=error_message)

    def test_clean_up_spacing(self):
        actual_result = clean_up_spacing("  A rolling stone gathers no moss")
        expected = "A rolling stone gathers no moss"
        error_message = (f'Called clean_up_spacing("  A rolling stone gathers no moss"). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" as a cleaned string.')

        self.assertEqual(actual_result, expected, msg=error_message)

    def test_replace_words_with_a_synonym(self):
        actual_result = replace_word_choice("Animals are cool.", "cool", "awesome")
        expected = "Animals are awesome."
        error_message = ('Called replace_word_choice("Animals are cool.", "cool", "awesome"). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" after the word replacement.')

        self.assertEqual(actual_result, expected, msg=error_message)
