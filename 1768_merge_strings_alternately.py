import unittest
from icecream import ic

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sol = ''
        len_word1 = len(word1)
        len_word2 = len(word2)
        max_len = max(len_word2, len_word1)
        for i in range(0, max_len):
            if i <= len_word1-1:
                sol += word1[i]
            if i <= len_word2-1:
                sol += word2[i]
        return sol
        

sol = Solution()
class Test(unittest.TestCase):
    def test1(self) -> None:
        assert sol.mergeAlternately(word1 = "abc", word2 = "pqr") == "apbqcr"

    def test2(self) -> None:
        assert sol.mergeAlternately(word1 = "ab", word2 = "pqrs") == "apbqrs"

    def test3(self) -> None:
        assert sol.mergeAlternately(word1 = "abcd", word2 = "pq") == "apbqcd"


if __name__ == '__main__':
    unittest.main(verbosity=2)
