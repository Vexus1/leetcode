import collections

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dict_ = collections.defaultdict(int)
        for i in nums:
            dict_[i] +=1

        n = len(nums) // 2
        for key, value in dict_.items():
            if value > n:
                return key
        
        return 0
            
solution = Solution()
print(solution.majorityElement([3,3,4]))

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
    
solution = Solution()
print(solution.majorityElement([3,3,4]))
