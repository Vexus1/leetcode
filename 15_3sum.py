# two pointers approach
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


# default dict approach (faster than two pointers approach)
from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        positives = defaultdict(int)
        negatives = defaultdict(int)
        zeros = 0
        for n in nums:
            if n > 0:
                positives[n] += 1
            elif n < 0:
                negatives[n] += 1
            else:
                zeros += 1
        
        result = []
        if zeros:
            for n in negatives.keys():
                if -n in positives.keys():
                    result.append([0, n, -n])
            if zeros > 2:
                result.append([0,0,0])
        
        for set1, set2 in ((negatives, positives), (positives, negatives)):
            set1_items = list(set1.items())
            for i, (j, k) in enumerate(set1_items):
                for j2, _ in set1_items[i:]:
                    if j != j2 or (j == j2 and k > 1):
                        if -j-j2 in set2:
                            result.append([j, j2, -j-j2])
        return result

sol = Solution()
print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))
print(sol.threeSum(nums = []))
print(sol.threeSum(nums = [0,0,0]))
