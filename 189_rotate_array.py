import unittest

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        nums_len = len(nums)
        k = k-(k//nums_len*nums_len)
        nums[nums_len-k:], nums[:nums_len-k] = nums[:nums_len-k], nums[nums_len-k:]
        return nums


sol = Solution()
class Test(unittest.TestCase):
    def test_1(self):
        assert sol.rotate(nums = [1,2,3,4,5,6,7], k = 5) == [3,4,5,6,7,1,2]
        print("PASSED: assert sol.rotate(nums = [1,2,3,4,5,6,7], k = 5) == [3,4,5,6,7,1,2]")

    def test_2(self):
        assert sol.rotate(nums = [-1,-100,3,99], k = 204) == [-1, -100, 3, 99]
        print("PASSED: assert sol.rotate(nums = [-1,-100,3,99], k = 204) == [-1, -100, 3, 99]")

    def test_3(self):
        assert sol.rotate(nums = [-1], k = 10) == [-1]
        print("PASSED: assert sol.rotate(nums = [-1], k = 10)) == [3,4,5,6,7,1,2] == [-1]")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("passed 3/3")
