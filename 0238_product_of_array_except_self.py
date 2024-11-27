class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        result = [1] * len_nums
        prefix = 1
        for i in range(len_nums):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len_nums-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result

sol = Solution()
print(sol.productExceptSelf(nums = [1,2,3,4])) # -> [24,12,8,6]
print(sol.productExceptSelf(nums = [-1,1,0,-3,3]))
