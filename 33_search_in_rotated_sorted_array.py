class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target and nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target and nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
    
sol = Solution()
print(sol.search(nums = [4,5,6,7,0,1,2], target = 0))
print(sol.search(nums = [4,5,6,7,0,1,2], target = 3))
print(sol.search(nums = [1], target = 0))
