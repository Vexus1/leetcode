class Solution:
    def reverseString(self, s: list[str]) -> None:
        i = 0
        j = len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


sol = Solution()
s = ["h","e","l","l","o"]
sol.reverseString(s)
print(s)
s = ["H","a","n","n","a","h"]
sol.reverseString(s)
print(s)
