import unittest
import numpy as np

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        matrix = [[] for row in range(numRows)]
        index = 0
        step = -1
        for char in s:
            matrix[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        return "".join(["".join(i) for i in matrix])


sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.convert(s = "PAYPALISHIRING", numRows = 3) == "PAHNAPLSIIGYIR"

    def test2(self):
        assert sol.convert(s = "PAYPALISHIRING", numRows = 4) == "PINALSIGYAHRPI"

    def test3(self):
        assert sol.convert(s = "A", numRows = 1) == "A"


if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 3/3')
