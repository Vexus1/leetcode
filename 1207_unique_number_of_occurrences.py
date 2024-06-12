import unittest
from icecream import ic
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        arr_map = Counter(arr)
        return len(arr_map.values()) == len(set(arr_map.values())) 


sol = Solution()
class Test(unittest.TestCase):
    def test1(self) -> None:
        assert sol.uniqueOccurrences(arr = [1,2,2,1,1,3]) == True
        
    def test2(self) -> None:
        assert sol.uniqueOccurrences(arr = [1,2]) == False

    def test3(self) -> None:
        assert sol.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]) == True


if __name__ == '__main__':
    unittest.main(verbosity=2)
