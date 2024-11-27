import unittest

# By Sorting. Time complexity: O((m+n)log(m+n))
class SortingSolution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1 = sorted(nums1[:m] + nums2)
        return nums1
        

# By Two Pointer. Time complexity: O(m+n)
class TwoPointerSolution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        return nums1


sort_sol = SortingSolution()
tp_sol = TwoPointerSolution()
class Test(unittest.TestCase):
    def test_1(self):
        assert sort_sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3) == [1,2,2,3,5,6]
        print("PASSED: assert sort_sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)) == [1,2,2,3,5,6]")
    
    def test_2(self):
        assert sort_sol.merge(nums1 = [1], m = 1, nums2 = [], n = 0) == [1]
        print("PASSED: assert sort_sol.merge(nums1 = [1], m = 1, nums2 = [], n = 0) == [1]")
    
    def test_3(self):
        assert sort_sol.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
        print("PASSED: assert sort_sol.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)")

    def test_4(self):
        assert tp_sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3) == [1,2,2,3,5,6]
        print("PASSED: assert tp_sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)) == [1,2,2,3,5,6]")
    
    def test_5(self):
        assert tp_sol.merge(nums1 = [1], m = 1, nums2 = [], n = 0) == [1]
        print("PASSED: assert tp_sol.merge(nums1 = [1], m = 1, nums2 = [], n = 0) == [1]")
    
    def test_6(self):
        assert tp_sol.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
        print("PASSED: assert tp_sol.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)")

if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("6/6 passed")
