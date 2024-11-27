import unittest

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits = int("".join(str(i) for i in digits))
        digits += 1
        return [int(i) for i in str(digits)]


sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.plusOne(digits = [1,2,3]) == [1,2,4]
        
    def test2(self):
        assert sol.plusOne(digits = [4,3,2,1]) == [4,3,2,2]
        
    def test3(self):
        assert sol.plusOne(digits = [9]) == [1,0]
        

if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 3/3')
