# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/

import unittest


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        s_vowels = []
        for char in s:
            if char in vowels:
                s_vowels.append(char)

        output = ''
        for char in s:
            if char in vowels:
                output += s_vowels.pop()
            else:
                output += char

        return output


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_example_1(self):
        s = "hello"
        self.assertEqual("holle", self.solution.reverseVowels(s))

    def test_example_2(self):
        s = "leetcode"
        self.assertEqual("leotcede", self.solution.reverseVowels(s))
