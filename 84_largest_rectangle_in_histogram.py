import unittest
from icecream import ic

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        largest_area = 0
        stack: list[tuple[int, int]] = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                largest_area = max(largest_area, height*(i-index))
                start = index
            stack.append((start, h)) 
        for i, h in stack:
            largest_area = max(largest_area, h*(len(heights)-i))
        return largest_area

sol = Solution()
class Test(unittest.TestCase):
    def test1(self) -> None:
        assert sol.largestRectangleArea(heights = [2,1,5,6,2,3]) == 10

    def test2(self) -> None:
        assert sol.largestRectangleArea(heights = [2,4]) == 4

if __name__ == '__main__':
    unittest.main(verbosity=2)
