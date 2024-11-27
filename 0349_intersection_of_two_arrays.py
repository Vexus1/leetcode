class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        num1_set = set(nums1)
        num2_set = set(nums2)
        result = []
        for n in num1_set:
            if n in num1_set and n in num2_set:
                result.append(n)
        return result

sol = Solution()
print(sol.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
print(sol.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))

# one line solution
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return set(nums1) & set(nums2)

sol = Solution()
print(sol.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
print(sol.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
