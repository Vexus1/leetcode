class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        s = [i for i in s if i != '']
        return len(s[-1])

sol = Solution()
print(sol.lengthOfLastWord(s = "Hello World"))
print(sol.lengthOfLastWord(s = "   fly me   to   the moon  "))
print(sol.lengthOfLastWord(s = "luffy is still joyboy"))
