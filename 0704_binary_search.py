import unittest

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            pivot = left + ((right - left)//2)
            if nums[pivot] < target:
                left = pivot + 1
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                return pivot
        return -1

sol = Solution()
class Test(unittest.TestCase):
    def test1(self) -> None:
        assert sol.search(nums = [-1,0,3,5,9,12], target = 9) == 4

    def test2(self) -> None:
        assert sol.search(nums = [-1,0,3,5,9,12], target = 2) == -1

if __name__ == '__main__':
    unittest.main(verbosity=2)
