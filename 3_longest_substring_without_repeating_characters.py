import unittest
# from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        repetitions = sorted(list(set(s)))
        rep_dict = {i: 0 for i in repetitions}
        # rep_dict = defaultdict()
        substrings_list = []
        substring = ''
        for i in range(len(s)):
            rep_dict = {i: 0 for i in repetitions}
            for char in s[i:]:
                # if char in repetitions:
                rep_dict[char] += 1
                # print(rep_dict)
                if rep_dict[char] > 1:
                    # substrings_list.append(substring)
                    substring = ''
                    rep_dict = {i: 0 for i in repetitions}
                    rep_dict[char] = 1
                # rep_dict[char] += 1
                substring += char
                # print(substring)
                # substrings_list.append(substring)
                substrings_list.append(substring)
        # print(substrings_list)
        print(substrings_list)
        # print(max(substrings_list))
        # return max(substrings_list)




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
    print("5/5 passed")
