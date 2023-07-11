class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

solution = Solution()
nums1 = [1,2,3,1]
nums2 = [1,2,3,4]

print(solution.containsDuplicate(nums1))
print(solution.containsDuplicate(nums2))

# difference between set and list
# Lists are slightly faster than sets when you just want to iterate over the values. 
# Sets, however, are significantly faster than lists if you want to check if an item is contained within it. 
# They can only contain unique items though.