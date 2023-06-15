# Link: https://leetcode.com/problems/reverse-words-in-a-string/

import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        s = "the sky is blue"
        self.assertEqual("blue is sky the", self.solution.reverseWords(s))

    def test_example_2(self):
        s = "  hello world  "
        self.assertEqual("world hello", self.solution.reverseWords(s))

    def test_example_3(self):
        s = "a good   example"
        self.assertEqual("example good a", self.solution.reverseWords(s))
