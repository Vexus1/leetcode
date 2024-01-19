import unittest

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        result = 0
        while left < right:
            current_area = min(height[left], height[right])*(right-left)
            result = max(result, current_area)
            if height[left] < height[right]:
                left += 1
            else:  
                right -= 1
        return result
        


sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.maxArea(height=[1,8,6,2,5,4,8,3,7]) == 49

    def test2(self):
        assert sol.maxArea(height=[1,1]) == 1

    def test3(self):
        assert sol.maxArea(height=[2,3,4,5,18,17,6]) == 17

if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 3/3')
