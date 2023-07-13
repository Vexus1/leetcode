class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i  
    
solution = Solution()
print(solution.twoSum(nums = [2,7,11,15], target = 9))
print(solution.twoSum(nums = [3,3], target = 6))
print(solution.twoSum(nums = [3,2,4], target = 6))
