class Solution:
    # Sets cannot have two items with the same value.
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        pattern_set = set(pattern)
        s_set = set(s)
        zipped_set = set(zip(pattern,s))
        return len(pattern_set) == len(s_set) == len(zipped_set) and len(s) == len(pattern)

solotion = Solution()
print(solotion.wordPattern(pattern = "abba", s = "dog cat cat dog"))
print(solotion.wordPattern(pattern = "abba", s = "dog cat cat fish"))
print(solotion.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
print(solotion.wordPattern(pattern = "abba", s = "dog dog dog dog"))
