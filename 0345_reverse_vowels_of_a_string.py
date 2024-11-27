class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)
    

sol = Solution()
print(sol.reverseVowels(s = "hello"))
print(sol.reverseVowels(s = "leetcode"))
print(sol.reverseVowels(s = "Aa"))
