import unittest

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


class Test(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        nums = [3,2,2,3]
        val = 3
        k = sol.removeElement(nums, val)
        assert ((k), sorted(nums[:k])) == (2, [2,2])
    
    def test_2(self):
        sol = Solution()
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        k = sol.removeElement(nums, val)
        assert ((k, sorted(nums[:k]))) == (5, [0,0,1,3,4])

if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("2/2 passed")
