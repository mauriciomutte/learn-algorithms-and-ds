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