# Link: https://leetcode.com/problems/greatest-common-divisor-of-strings

import unittest


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        dividend = str1
        divisor = str2

        while dividend != divisor:
            if len(dividend) < len(divisor):
                dividend, divisor = divisor, dividend

            parts = [dividend[:len(divisor)], dividend[len(divisor):]]

            if divisor in parts:
                parts.remove(divisor)
                dividend = divisor
                divisor = parts[0]
            else:
                return ""

        return divisor


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        str1 = "ABCABC"
        str2 = "ABC"
        self.assertEqual("ABC", self.solution.gcdOfStrings(str1, str2))

    def test_example_2(self):
        str1 = "ABABAB"
        str2 = "ABAB"
        self.assertEqual("AB", self.solution.gcdOfStrings(str1, str2))

    def test_example_3(self):
        str1 = "LEET"
        str2 = "CODE"
        self.assertEqual("", self.solution.gcdOfStrings(str1, str2))

    def test_example_4(self):
        str1 = "ABCDEF"
        str2 = "ABC"
        self.assertEqual("", self.solution.gcdOfStrings(str1, str2))

    def test_example_5(self):
        str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
        str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
        self.assertEqual("TAUXX", self.solution.gcdOfStrings(str1, str2))

    def test_example_6(self):
        str1 = "ABABABAB"
        str2 = "ABAB"
        self.assertEqual("ABAB", self.solution.gcdOfStrings(str1, str2))

    def test_example_7(self):
        str1 = "EFGABC"
        str2 = "ABC"
        self.assertEqual("", self.solution.gcdOfStrings(str1, str2))
