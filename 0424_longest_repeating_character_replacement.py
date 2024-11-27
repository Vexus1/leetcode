import unittest
from collections import defaultdict
from icecream import ic

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_count = 0
        left = 0 
        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(count[s[right]], max_count)
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
        return right - left + 1


sol = Solution()
class Test(unittest.TestCase):
    def test1(self) -> None:
        assert sol.characterReplacement(s="ABAB", k=2) == 4 

    def test2(self) -> None:
        assert sol.characterReplacement(s="AABABBA", k=1) == 4 

    def test3(self) -> None:
        assert sol.characterReplacement(s="ABAA", k=0) == 2


if __name__ == '__main__':
    unittest.main(verbosity=2)
