class Solution:
     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = [] 

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                res[stack_index] = i - stack_index
            stack.append((temp, i))
        return res

sol = Solution()
print(sol.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
print(sol.dailyTemperatures(temperatures = [30,40,50,60]))
print(sol.dailyTemperatures(temperatures = [30,60,90]))

# solution using deque
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures):
        res, d = [0]*len(temperatures), deque()
        for i, temp in enumerate(temperatures):
            while d and temp > temperatures[d[-1]]:
                res[d[-1]] = i - d[-1]
                d.pop()
            d.append(i)
        return res
    
sol = Solution()
print(sol.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
print(sol.dailyTemperatures(temperatures = [30,40,50,60]))
print(sol.dailyTemperatures(temperatures = [30,60,90]))
