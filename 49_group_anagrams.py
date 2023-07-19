# using sorting
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            result[sorted_word].append(word)
        return list(result.values())

sol = Solution()
print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams(strs = [""]))
print(sol.groupAnagrams(strs = ["a"]))

# using Unicode
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            result[tuple(count)].append(word)
        return result.values()

sol = Solution()
print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams(strs = [""]))
print(sol.groupAnagrams(strs = ["a"]))
