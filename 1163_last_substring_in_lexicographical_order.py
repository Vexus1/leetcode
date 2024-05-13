import unittest
from string import ascii_lowercase

class Solution:
    def lastSubstring(self, s: str) -> str:
        char_map = {char: i for i, char in enumerate(ascii_lowercase)}
        left = 0
        right = len(s) - 1
        while left < right:
            pass


sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.lastSubstring(s = "abab") == "bab"
        # The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".

    def test2(self):
        assert sol.lastSubstring(s = "leetcode") == "tcode"


if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 2/2')
