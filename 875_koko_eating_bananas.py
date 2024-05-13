import unittest
from icecream import ic
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = left
        while left <= right:
            mid = (right + left)//2
            time = 0
            for banana in piles:
                time += ceil(banana/mid)
            if time <= h:
                res = mid
                right = mid-1
            else:
                left = mid+1
        return res

sol = Solution()
class Test(unittest.TestCase):
    def test1(self) -> None:
        assert sol.minEatingSpeed(piles = [3,6,7,11], h = 8) == 4

    def test2(self) -> None:
        assert sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5) == 30

    def test3(self) -> None:
        assert sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6) == 23


if __name__ == '__main__':
    unittest.main(verbosity=2)
