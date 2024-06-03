import unittest
from icecream import ic

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)-1
        ans = float('inf')
        while left <= right:
            mid = (left + right) // 2
            ans = min(ans, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return ans


sol = Solution()
class Test(unittest.TestCase):
    def test1(self) -> None:
        assert sol.findMin(nums = [3,4,5,1,2]) == 1

    def test2(self) -> None:
        assert sol.findMin(nums = [4,5,6,7,0,1,2]) == 0

    def test3(self) -> None:
        assert sol.findMin(nums = [11,13,15,17]) == 11


if __name__ == '__main__':
    unittest.main(verbosity=2)
