import unittest

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        first = 0 
        last = len(numbers)-1
        while first <= last:
            if numbers[first] + numbers[last] == target:
                return [first+1, last+1]
            if numbers[first] + numbers[last] < target:
                first += 1
            else:
                last -= 1
        

sol = Solution()
class test(unittest.TestCase):
    def test1(self):
        assert sol.twoSum(numbers = [2,7,11,15], target = 9) == [1,2]

    def test2(self):
        assert sol.twoSum(numbers = [2,3,4], target = 6) == [1,3]

    def test3(self):
        assert sol.twoSum(numbers = [-1,0], target = -1) == [1,2]

    def test4(self):
        assert sol.twoSum(numbers = [2,7,10,11,15], target = 9) == [1,2]

    def test5(self):
        assert sol.twoSum(numbers = [0,0,3,4], target = 0) == [1,2]

if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 4/4')
