class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]: # skip duplicates of first value
                continue
            first = nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                second = nums[j]
                third = nums[k]
                sum = first + second + third
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    result.add((first, second, third))
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]: 
                        j += 1 # skip duplicates of second value
                    while j < k and nums[k+1] == nums[k]:
                        k -= 1 # skip duplicates of third value
        return list(list(i) for i in result)

            

sol = Solution()
print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))
print(sol.threeSum(nums = []))
print(sol.threeSum(nums = [0,0,0]))
