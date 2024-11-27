import unittest

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.reverseWords(s = "the sky is blue") == "blue is sky the"

    def test2(self):
        assert sol.reverseWords(s = "  hello world  ") == "world hello"

    def test3(self):
        assert sol.reverseWords(s = "a good   example") == "example good a"

if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 3/3')

    