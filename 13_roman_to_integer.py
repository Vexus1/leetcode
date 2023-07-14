class Solution:
    def romanToInt(self, s: str) -> int:
        map_symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                       'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and map_symbols[s[i+1]] > map_symbols[s[i]]:
                result -= map_symbols[s[i]]
            else:
                result += map_symbols[s[i]]
        return result


solution = Solution()
print(solution.romanToInt(s = "LVIII"))