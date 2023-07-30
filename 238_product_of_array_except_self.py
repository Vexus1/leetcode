from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        dict_ = defaultdict(int)
        for n in nums:
            dict_[n] += 1
        
sol = Solution()
print(sol.productExceptSelf(nums = [1,2,3,4]))
print(sol.productExceptSelf(nums = [-1,1,0,-3,3]))
