import unittest


class Solution:
    def can_place_flowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        empty = 0
        prev = None
        for i, s in enumerate(flowerbed):
            nxt = flowerbed[i + 1] if i + 1 < len(flowerbed) else None
            if s == 0 and prev != 1 and nxt != 1:
                prev = 1
                empty += 1
                if empty == n:
                    return True
            else:
                prev = s

        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self) -> None:
        flowerbed = [1, 0, 0, 0, 1]
        n = 1
        expected = True
        self.assertEqual(self.solution.can_place_flowers(flowerbed, n), expected)
    
    def test_example_2(self) -> None:
        flowerbed = [1, 0, 0, 0, 1]
        n = 2
        expected = False
        self.assertEqual(self.solution.can_place_flowers(flowerbed, n), expected)

    def test_example_3(self) -> None:
        flowerbed = [0, 0, 1, 0, 1]
        n = 1
        expected = True
        self.assertEqual(self.solution.can_place_flowers(flowerbed, n), expected)

    def test_example_4(self) -> None:
        flowerbed = [1, 0, 0, 0, 0, 0, 1]
        n = 2
        expected = True
        self.assertEqual(self.solution.can_place_flowers(flowerbed, n), expected)

    def test_example_5(self) -> None:
        flowerbed = [0, 0, 1, 0, 1]
        n = 1
        expected = True
        self.assertEqual(self.solution.can_place_flowers(flowerbed, n), expected)

    def test_example_6(self) -> None:
        flowerbed = [1, 0, 0, 0, 0, 1]
        n = 2
        expected = False
        self.assertEqual(self.solution.can_place_flowers(flowerbed, n), expected)

