import unittest


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        """ arguments of type float or str cause a TypeError exception """
        cases = ('string',  1.5)
        for x in cases:
            with self.subTest(case=x):
                with self.assertRaises(TypeError):
                    factorize(x)

    def test_negative(self):
        """ negative numbers cause ValueError exception """
        cases = (-1,  -10,  -100)
        for x in cases:
            with self.subTest(case=x):
                with self.assertRaises(ValueError):
                    factorize(x)

    def test_zero_and_one_cases(self):
        """ the integers 0 and 1, return the tuples (0,) and (1,) respectively. """
        for x, fact_x in (0, (0, )),  (1, (1, )):
            with self.subTest(case=x):
                self.assertEqual(factorize(x), fact_x)

    def test_simple_numbers(self):
        """ it returns a tuple containing the single given number for prime numbers """
        for x in 3, 13, 29:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_two_simple_multipliers(self):
        """ for these numbers the factorize function returns a tuple of size 2 """
        test_cases = (
            (6, (2, 3)),
            (26, (2, 13)),
            (121, (11, 11)),
        )
        for x, fact_x in test_cases:
            with self.subTest(case=x):
                self.assertEqual(factorize(x), fact_x)

    def test_many_multipliers(self):
        """ for these numbers the factorize function returns a tuple of size >2 """
        for x, fact_x in (1001, (7, 11, 13)), \
                         (9699690, (2, 3, 5, 7, 11, 13, 17, 19)):
            with self.subTest(case=x):
                self.assertEqual(factorize(x), fact_x)


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass


if __name__ == '__main__':
    unittest.main()
