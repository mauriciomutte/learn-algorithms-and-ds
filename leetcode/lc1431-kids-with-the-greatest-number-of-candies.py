# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

import unittest


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        greatestNumber = sorted(candies)[-1]

        result = []
        for candiesWithKid in candies:
            if (candiesWithKid + extraCandies) >= greatestNumber:
                result.append(True)
            else:
                result.append(False)

        return result


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        candies = [2, 3, 5, 1, 3]
        extraCandies = 3
        self.assertEqual([True, True, True, False, True], self.solution.kidsWithCandies(candies, extraCandies))

    def test_example_2(self):
        candies = [4, 2, 1, 1, 2]
        extraCandies = 1
        self.assertEqual([True, False, False, False, False], self.solution.kidsWithCandies(candies, extraCandies))

    def test_example_3(self):
        candies = [12, 1, 12]
        extraCandies = 10
        self.assertEqual([True, False, True], self.solution.kidsWithCandies(candies, extraCandies))