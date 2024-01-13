from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = defaultdict(int)
        for i in magazine:
            magazine_dict[i] += 1
        for i in ransomNote:
            magazine_dict[i] -= 1
        for i in magazine_dict.values():
            if i < 0:
                return False
        return True

sol = Solution()
print(sol.canConstruct(ransomNote = "a", magazine = "b"))
print(sol.canConstruct(ransomNote = "aa", magazine = "ab"))
print(sol.canConstruct(ransomNote = "aa", magazine = "aab"))
