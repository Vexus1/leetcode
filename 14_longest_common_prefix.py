class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs = sorted(strs)
        ans = ''
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans
    
sol = Solution()
print(sol.longestCommonPrefix(strs = ["flower","flow","flight"]))
print(sol.longestCommonPrefix(strs = ["dog","racecar","car"]))
