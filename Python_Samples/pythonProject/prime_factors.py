import unittest


def factors(value):
    l_num = []
    if value == 2 or value == 3:
        l_num = [value]

    stop = value//2
    index = 2
    while index <= stop:
        if value % index == 0:
            value /= index
            l_num.append(index)
        else:
            if index == 2:
                index += 1
            else:
                index += 2

        stop = value if value == 1 else stop

    return l_num
    pass


class PrimeFactorsTest(unittest.TestCase):
    def test_no_factors(self):
        self.assertEqual(factors(1), [])

    def test_prime_number(self):
        self.assertEqual(factors(2), [2])

    def test_another_prime_number(self):
        self.assertEqual(factors(3), [3])

    def test_square_of_a_prime(self):
        self.assertEqual(factors(9), [3, 3])

    def test_product_of_first_prime(self):
        self.assertEqual(factors(4), [2, 2])

    def test_cube_of_a_prime(self):
        self.assertEqual(factors(8), [2, 2, 2])

    def test_product_of_second_prime(self):
        self.assertEqual(factors(27), [3, 3, 3])

    def test_product_of_third_prime(self):
        self.assertEqual(factors(625), [5, 5, 5, 5])

    def test_product_of_first_and_second_prime(self):
        self.assertEqual(factors(6), [2, 3])

    def test_product_of_primes_and_non_primes(self):
        self.assertEqual(factors(12), [2, 2, 3])

    def test_product_of_primes(self):
        self.assertEqual(factors(901255), [5, 17, 23, 461])

    def test_factors_include_a_large_prime(self):
        self.assertEqual(factors(93819012551), [11, 9539, 894119])
