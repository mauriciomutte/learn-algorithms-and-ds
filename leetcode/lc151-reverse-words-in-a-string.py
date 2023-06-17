# Link: https://leetcode.com/problems/reverse-words-in-a-string/

import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        temp_word = ""
        for c in s:
            if c != " ":
                temp_word += c
            elif temp_word != "":
                words.append(temp_word)
                temp_word = ""

        if temp_word != "":
            words.append(temp_word)

        i = 0
        j = len(words) - 1
        while i < j:
            temp = words[i]
            words[i] = words[j]
            words[j] = temp
            i += 1
            j -= 1

        return " ".join(words)


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
