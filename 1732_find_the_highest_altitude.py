import unittest

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alitude = [0]
        for n in gain:
            temp = alitude[-1]
            alitude.append(temp+n)
        return max(alitude)
    

sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.largestAltitude(gain = [-5,1,5,0,-7]) == 1

    def test2(self):
        assert sol.largestAltitude(gain = [-4,-3,-2,-1,4,3,2]) == 0


if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 2/2')
