class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        return s == s[::-1]

    
sol = Solution()
print(sol.isPalindrome(s = "A man, a plan, a canal: Panama"))
print(sol.isPalindrome(s = "race a car"))
print(sol.isPalindrome(s = " "))