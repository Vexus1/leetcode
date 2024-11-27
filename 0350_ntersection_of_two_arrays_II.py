class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for n in nums1:
            try:
                nums2.remove(n)
                result.append(n)
            except:
                continue
        return result
    
sol = Solution()
print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2]))


from collections import defaultdict
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_dict, nums2_dict = defaultdict(int), defaultdict(int)
        for n in nums1:
            nums1_dict[n] += 1
        for n in nums2:
            nums2_dict[n] += 1

        result = []
        for n in nums1_dict:
            if n in nums2_dict:
                count = min(nums1_dict[n], nums2_dict[n])
                result.extend([n] * count)

        return result

sol = Solution()
print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2]))
