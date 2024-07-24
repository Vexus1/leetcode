import unittest

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = 0
        max_altitude = 0
        for n in gain:
            altitude += n
            max_altitude = max(max_altitude, altitude)
        return max_altitude
    

sol = Solution()
class Test(unittest.TestCase):
    def test1(self) -> None:
        assert sol.largestAltitude(gain = [-5,1,5,0,-7]) == 1

    def test2(self) -> None:
        assert sol.largestAltitude(gain = [-4,-3,-2,-1,4,3,2]) == 0


if __name__ == '__main__':
    unittest.main(verbosity=2)
