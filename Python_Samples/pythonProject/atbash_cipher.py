import string
import unittest


def encode(plain_text):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    result = ""
    counter = 0
    for ch in plain_text:
        temp = ch
        if ch in lower:
            temp = chr((ord('z') - ord(ch)) + ord('a'))
            counter += 1
        elif ch in upper:
            temp = chr((ord('Z') - ord(ch)) + ord('A'))
            counter += 1
        elif ch.isspace() or ch in ",.":
            temp = ""
        elif ch.isdigit():
            temp = ch
            counter += 1

        result = result + temp
        if counter == 5:
            counter = 0
            result = result + " "

    return result.lower().rstrip()


def decode(ciphered_text):
    result = ""
    lower = string.ascii_lowercase

    for ch in ciphered_text:
        temp = ch
        if ch in lower:
            temp = chr((ord('z') - ord(ch)) + ord('a'))
        elif ch.isspace():
            temp = ""
        result = result + temp
    return result


class AtbashCipherTest(unittest.TestCase):
    def test_encode_yes(self):
        self.assertEqual(encode("yes"), "bvh")
    def test_encode_no(self):
        self.assertEqual(encode("no"), "ml")
    def test_encode_omg(self):
        self.assertEqual(encode("OMG"), "lnt")
    def test_encode_spaces(self):
        self.assertEqual(encode("O M G"), "lnt")
    def test_encode_mindblowingly(self):
        self.assertEqual(encode("mindblowingly"), "nrmwy oldrm tob")
    def test_encode_numbers(self):
        self.assertEqual(encode("Testing,1 2 3, testing."), "gvhgr mt123 gvhgr mt")
    def test_encode_deep_thought(self):
        self.assertEqual(encode("Truth is fiction."), "gifgs rhurx grlm")
    def test_encode_all_the_letters(self):
        self.assertEqual(
            encode("The quick brown fox jumps over the lazy dog."),
            "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt",
        )
    def test_decode_exercism(self):
        self.assertEqual(decode("vcvix rhn"), "exercism")
    def test_decode_a_sentence(self):
        self.assertEqual(
            decode("zmlyh gzxov rhlug vmzhg vkkrm thglm v"),
            "anobstacleisoftenasteppingstone",
        )
    def test_decode_numbers(self):
        self.assertEqual(decode("gvhgr mt123 gvhgr mt"), "testing123testing")
    def test_decode_all_the_letters(self):
        self.assertEqual(
            decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"),
            "thequickbrownfoxjumpsoverthelazydog",
        )
    def test_decode_with_too_many_spaces(self):
        self.assertEqual(decode("vc vix    r hn"), "exercism")
    def test_decode_with_no_spaces(self):
        self.assertEqual(
            decode("zmlyhgzxovrhlugvmzhgvkkrmthglmv"), "anobstacleisoftenasteppingstone"
        )