class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return left
    
s = Solution()
print(s.searchInsert(nums = [1,3,5,6], target = 5))
print(s.searchInsert(nums = [1,3,5,6], target = 2))
print(s.searchInsert(nums = [1,3,5,6], target = 7))
