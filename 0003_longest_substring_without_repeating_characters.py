import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        char_set = []
        left = 0
        for right in range(len(s)):
            if s[right] not in char_set:
                char_set.append(s[right])
                max_len = max(max_len, right - left + 1)
            else:
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1
                char_set.append(s[right])
        return max_len
        

sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.lengthOfLongestSubstring(s = "abcabcbb") == 3

    def test2(self):
        assert sol.lengthOfLongestSubstring(s = "bbbbb") == 1

    def test3(self):
        assert sol.lengthOfLongestSubstring(s = "pwwkew") == 3

    def test4(self):
        assert sol.lengthOfLongestSubstring(s = "") == 0

    def test5(self):
        assert sol.lengthOfLongestSubstring(s = "dvdf") == 3

    def test6(self):
        assert sol.lengthOfLongestSubstring(s = "asjrgapa") == 6

if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("6/6 passed")
