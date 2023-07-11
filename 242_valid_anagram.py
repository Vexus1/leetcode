# Sorting - time complexity of O(n log n).
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t
        
solution = Solution()
s1 = "anagram"
t1 = "nagaram"
s2 = "rat"
t2 = "car"
print(solution.isAnagram(s1,t1))
print(solution.isAnagram(s2,t2))


# Hash Table - Time complexity of O(n).
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}
        
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        return count_s == count_t

solution = Solution()
s1 = "anagram"
t1 = "nagaram"
s2 = "rat"
t2 = "car"
print(solution.isAnagram(s1,t1))
print(solution.isAnagram(s2,t2))


# Hash Table (using arrays) - Time complexity of O(n).
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        
        for x in s:
            count[ord(x) - ord('a')] += 1 # The ord() function returns the number representing the unicode code of a specified character.
            print(count)
        
        for x in t:
            count[ord(x) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        
        return True
    
solution = Solution()
s1 = "anagram"
t1 = "nagaram"
s2 = "rat"
t2 = "car"
print(solution.isAnagram(s1,t1))
print(solution.isAnagram(s2,t2))
