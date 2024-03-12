import unittest

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:len(needle)+i] == needle:
                return i
        return -1


sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.strStr(haystack = "sadbutsad", needle = "sad") == 0

    def test2(self):
        assert sol.strStr(haystack = "leetcode", needle = "leeto") == -1

    def test3(self):
        assert sol.strStr(haystack = "mississippi", needle = "issip" ) == 4


if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 2/2')
