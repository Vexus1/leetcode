import unittest
from collections import defaultdict
from icecream import ic
from numpy import transpose

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_map = defaultdict(int)
        col_map = defaultdict(int)
        sol = 0
        grid_transpose = transpose(grid)
        for row in grid:
            row_map[tuple(row)] += 1
        for col in grid_transpose:
            col_map[tuple(col)] += 1 
        for row in row_map:
            if row in col_map:
                sol += row_map[row] * col_map[row]
        return sol


sol = Solution()
class Test(unittest.TestCase):
    def test1(self) -> None:
        assert sol.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]]) == 1
        
    def test2(self) -> None:
        assert sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3


if __name__ == '__main__':
    unittest.main(verbosity=2)

