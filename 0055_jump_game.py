import unittest

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        jump = 0
        for n in nums:
            if jump < 0:
                return False
            elif n > jump:
                jump = n
            jump -= 1
        return True

solution = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert solution.canJump(nums = [2,3,1,1,4]) == True

    def test2(self):
        assert solution.canJump(nums = [3,2,1,0,4]) == False

    def test3(self):
        assert solution.canJump(nums = [0]) == True

if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 3/3')