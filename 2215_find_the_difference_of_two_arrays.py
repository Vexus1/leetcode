import unittest
from icecream import ic

class Solution:
    def findDifference(self, nums1: list[int],
                             nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1-set2), list(set2-set1)]
            

sol = Solution()
class Test(unittest.TestCase):
    def test1(self) -> None:
        assert sol.findDifference(nums1 = [1,2,3],
                                  nums2 = [2,4,6]) == [[1,3],[4,6]]
        
    def test2(self) -> None:
        assert sol.findDifference(nums1 = [1,2,3,3], 
                                  nums2 = [1,1,2,2]) == [[3],[]]

if __name__ == '__main__':
    unittest.main(verbosity=2)
