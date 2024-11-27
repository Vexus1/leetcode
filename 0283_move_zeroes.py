import unittest
from icecream import ic

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        return nums


sol = Solution()
class Test(unittest.TestCase):
    def test1(self) -> None:
        assert sol.moveZeroes(nums = [0,1,0,3,12]) == [1,3,12,0,0]

    def test2(self) -> None:
        assert sol.moveZeroes(nums = [0]) == [0]

    def test3(self) -> None:
        assert sol.moveZeroes(nums = [0,0,1]) == [1,0,0]

    def test4(self) -> None:
        assert sol.moveZeroes(nums = [1,0,1]) == [1,1,0]


if __name__ == '__main__':
    unittest.main(verbosity=2)
