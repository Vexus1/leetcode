from collections import defaultdict 
class Solution:
    def secondHighest(self, s: str) -> int:
        s_array = []
        s_dict = defaultdict(int)
        for i in s:
            if i.isdigit():
                integer = int(i)
                s_array.append(integer)

        if s_array != []:
            for i in s_array: 
                s_dict[i] += 1
        else:
            return -1
        
        s_dict.pop(max(s_array))
        if s_dict == {}:
            return -1
        else:
            return max(s_dict)

solution = Solution()
print(solution.secondHighest(s = "dfa12321afd"))
print(solution.secondHighest(s = "abc1111"))


# without dict and simpler soloution (same time complexity o(n))
class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1
        for i in s:
            if i.isdigit():
                integer = int(i)
                if integer > first:
                    first, second = integer, first
                elif first > integer > second:
                    second = integer
        return second

solution = Solution()
print(solution.secondHighest(s = "dfa12321afd"))
print(solution.secondHighest(s = "abc1111"))
