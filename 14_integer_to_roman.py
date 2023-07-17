from math import floor
class Solution:
    def intToRoman(self, num):
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hrns = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        ths =  ["", "M", "MM", "MMM"]

        return ths[floor(num / 1000)] + hrns[floor((num % 1000) / 100)] + tens[floor((num % 100) / 10)] + ones[floor(num % 10)]

solution = Solution()
print(solution.intToRoman(num = 58))