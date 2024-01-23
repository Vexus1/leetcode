import unittest

class Solution:
    def trap(self, height: list[int]) -> int:
        result = 0
        left = 0
        right = len(height)-1
        max_left = height[left]
        max_right = height[right]
        while left < right:
            if max_left <= max_right:
                left += 1
                max_left = max(max_left, height[left])
                result += max_left - height[left] 
            else:
                right -= 1 
                max_right = max(max_right, height[right])
                result += max_right - height[right] 
        return result


sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]) == 6
        
    def test2(self):
        assert sol.trap(height = [4,2,0,3,2,5]) == 9


if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 2/2')
