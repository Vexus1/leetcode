class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        temp = nums[0]
        ans = []
        for i in range(nums):
            if nums[i+1] != temp+1:
                ans.append(str(temp))
                temp = temp[i+1]

sol = Solution()
print(sol.summaryRanges(nums = [0,1,2,4,5,7]))
print(sol.summaryRanges(nums = [0,2,3,4,6,8,9]))
