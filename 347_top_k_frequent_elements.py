
# O(n)
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dict_ = defaultdict(int)
        for num in nums:
            dict_[num] += 1

        result = []
        for _ in range(len(dict_)):
            if k > 0:
                max_val = max(dict_.values())
                values_arr = list(dict_.values())
                max_key_by_value = list(dict_.keys())[values_arr.index(max_val)]
                result.append(max_key_by_value)
                dict_[max_key_by_value] = 0
                k -= 1

        return result

sol = Solution()
print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(sol.topKFrequent(nums = [1], k = 1))
print(sol.topKFrequent(nums = [4,1,-1,2,-1,2,3], k = 2))
print(sol.topKFrequent(nums = [5,3,1,1,1,3,73,1], k = 2))
print(sol.topKFrequent(nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], k = 10))


# O(n) without collections library
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
sol = Solution()
print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(sol.topKFrequent(nums = [1], k = 1))
print(sol.topKFrequent(nums = [4,1,-1,2,-1,2,3], k = 2))
print(sol.topKFrequent(nums = [5,3,1,1,1,3,73,1], k = 2))
print(sol.topKFrequent(nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], k = 10))
