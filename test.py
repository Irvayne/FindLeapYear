import unittest
from leap_year import find_leap_year

class TestLeapYear(unittest.TestCase):

    def test_leap_year(self):
        self.assertEqual(find_leap_year(1600), True)
        self.assertEqual(find_leap_year(1732), True)
        self.assertEqual(find_leap_year(1888), True)
        self.assertEqual(find_leap_year(1944), True)
        self.assertEqual(find_leap_year(2008), True)

    def test_no_leap_year(self):
        self.assertEqual(find_leap_year(1742), False)
        self.assertEqual(find_leap_year(1889), False)
        self.assertEqual(find_leap_year(1951), False)
        self.assertEqual(find_leap_year(2011), False)


if __name__ == '__main__':
    unittest.main()
