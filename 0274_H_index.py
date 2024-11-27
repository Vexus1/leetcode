import unittest

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for citation in citations:
            if h < citation:
                h += 1
            else:
                return h
        return h


sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.hIndex(citations = [3,0,6,1,5]) == 3
    
    def test2(self):
        assert sol.hIndex(citations = [1,3,1]) == 1

    def test3(self):
        assert sol.hIndex(citations = [1]) == 1

    def test4(self):
        assert sol.hIndex(citations = [0]) == 0

    def test5(self):
        assert sol.hIndex(citations = [1,1]) == 1

    def test6(self):
        assert sol.hIndex(citations = [0,0]) == 0

    def test7(self):
        assert sol.hIndex(citations = [11,15]) == 2
    
    def test8(self):
        assert sol.hIndex(citations = [2,2]) == 2

if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 7/7')
