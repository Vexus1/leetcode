class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        set_nums = set(nums)
        return [n for n in range(1, len(nums)+1) if n not in set_nums]

sol = Solution()
print(sol.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))
print(sol.findDisappearedNumbers(nums = [1,1]))