import unittest


def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")
    if number == 1:
        return 2
    if number == 2:
        return 3

    p = 2
    counter = 2
    natural = 3
    while counter < number:
        natural += 2
        if is_prime(natural):
            p = natural
            counter += 1

    return p


def is_prime(n):
    flag = True
    for i in range(3, n // 2, 2):
        if n % i == 0:
            flag = False
            break
    return flag


class NthPrimeTest(unittest.TestCase):
    def test_first_prime(self):
        self.assertEqual(prime(1), 2)

    def test_second_prime(self):
        self.assertEqual(prime(2), 3)

    def test_sixth_prime(self):
        self.assertEqual(prime(6), 13)

    def test_big_prime(self):
        self.assertEqual(prime(10001), 104743)

    def test_there_is_no_zeroth_prime(self):
        with self.assertRaises(ValueError) as err:
            prime(0)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "there is no zeroth prime")
