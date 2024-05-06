import unittest
from icecream import ic

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1
        while top <= bottom:
            row = (bottom + top)//2
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bottom = row-1
            else:
                break
        row = matrix[row]
        left = 0
        right = len(row)-1
        ic(row)
        while left <= right:
            pivot = left + ((right - left)//2)
            if row[pivot] < target:
                left = pivot + 1
            elif row[pivot] > target:
                right = pivot - 1
            else:
                return True
        return False


sol = Solution()
class test(unittest.TestCase):
    def test1(self) -> None:
        assert sol.searchMatrix(matrix = [[1,3,5,7],
                                          [10,11,16,20],
                                          [23,30,34,60]],
                                           target = 3) == True
        
    def test2(self) -> None:
        assert sol.searchMatrix(matrix = [[1,3,5,7],
                                          [10,11,16,20],
                                          [23,30,34,60]], 
                                          target = 13) == False

    def test3(self) -> None:
        assert sol.searchMatrix(matrix = [[1],[3]], target = 2) == False
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
