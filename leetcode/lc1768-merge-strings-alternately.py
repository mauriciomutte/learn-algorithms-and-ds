# Link: https://leetcode.com/problems/merge-strings-alternately

import unittest


class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        result = []
        min_length = min(len(word1), len(word2))

        for i in range(min_length):
            result.append(word1[i])
            result.append(word2[i])

        output = "".join(result)

        if min_length < len(word1):
            return output + word1[min_length:]
        elif min_length < len(word2):
            return output + word2[min_length:]
        else:
            return output


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        word1 = "abc"
        word2 = "pqr"
        self.assertEqual("apbqcr", self.solution.merge_alternately(word1, word2))

    def test_example_2(self):
        word1 = "ab"
        word2 = "pqrs"
        self.assertEqual("apbqrs", self.solution.merge_alternately(word1, word2))

    def test_example_3(self):
        word1 = "abcd"
        word2 = "pq"
        self.assertEqual("apbqcd", self.solution.merge_alternately(word1, word2))

    def test_example_4(self):
        word1 = "abcdefghi"
        word2 = "pq"
        self.assertEqual("apbqcdefghi", self.solution.merge_alternately(word1, word2))
