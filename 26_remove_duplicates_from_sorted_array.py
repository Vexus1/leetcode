import unittest

# using set and sorted
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)
    

# without sorted
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
    

class Test(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        nums = [1,1,2]
        k = sol.removeDuplicates(nums)
        assert ((k), nums[:k]) == (2, [1,2])
        print("PASSED: assert ((k), nums[:k]) == (2, [1,2])")
    
    def test_2(self):
        sol = Solution()
        nums = [0,0,1,1,1,2,2,3,3,4]
        k = sol.removeDuplicates(nums)
        assert ((k, nums[:k])) == (5, [0,1,2,3,4])
        print("PASSED: assert ((k, nums[:k])) == (5, [0,1,2,3,4])")
    
    def test_3(self):
        sol = Solution()
        nums = [-1,0,0,0,3,3,3]
        k = sol.removeDuplicates(nums)
        assert ((k, nums[:k])) == (3, [-1,0,3])
        print("PASSED: assert ((k, nums[:k])) == (3, [-1,0,3])")

if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("3/3 passed")
