class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in num_set:
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(length, longest)
        return longest
        

    
s = Solution()
print(s.longestConsecutive(nums = [100,4,200,1,3,2]))
print(s.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive(nums = []))
print(s.longestConsecutive(nums = [0,-1]))
print(s.longestConsecutive(nums = [9,1,4,7,3,-1,0,5,8,-1,6]))


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        uniques = set(nums)
        max_length = 0
        while uniques:
            low = high = uniques.pop()
            while low - 1 in uniques or high + 1 in uniques:
                if low - 1 in uniques:
                    uniques.remove(low - 1)
                    low -= 1
                if high + 1 in uniques:
                    uniques.remove(high + 1)
                    high += 1
            max_length = max(high - low + 1, max_length)
        return max_length

s = Solution()
print(s.longestConsecutive(nums = [100,4,200,1,3,2]))
print(s.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive(nums = []))
print(s.longestConsecutive(nums = [0,-1]))
print(s.longestConsecutive(nums = [9,1,4,7,3,-1,0,5,8,-1,6]))
