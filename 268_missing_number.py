class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result = 0
        for i in range(len(nums)+1):
            result += i
        for n in nums:
            result -= n

        return result
    
sol = Solution()
print(sol.missingNumber(nums = [3,0,1]))
print(sol.missingNumber(nums = [0,1]))
print(sol.missingNumber(nums = [9,6,4,2,3,5,7,0,1]))
