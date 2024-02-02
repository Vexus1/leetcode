from collections import defaultdict

# Defoultdict approach
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = len(nums)
        nums_dict = defaultdict(int)
        for i in nums:
            nums_dict[i] += 1
        for key, value in nums_dict.items():
            if value > 2:
                temp = value
                while temp > 2:
                    nums.remove(key)
                    nums += ['_']
                    k -= 1
                    temp -= 1
        return k
    
sol = Solution()
print(sol.removeDuplicates(nums = [1,1,1,2,2,3]))
print(sol.removeDuplicates(nums = [0,0,1,1,1,1,2,3,3]))


# Two pointers approach
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        occur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                occur += 1
            else:
                occur = 1
            if occur <= 2:
                nums[k] = nums[i]
                k += 1
        nums[k:] = ['_' for i in range(len(nums)-k)]
        return k

sol = Solution()
print(sol.removeDuplicates(nums = [1,1,1,2,2,3]))
print(sol.removeDuplicates(nums = [0,0,1,1,1,1,2,3,3]))
