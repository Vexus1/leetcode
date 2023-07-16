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
            
solution = Solution()
print(solution.majorityElement([3,3,4]))