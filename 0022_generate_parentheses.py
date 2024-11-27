# Solution by DFS algorithm
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(left, right, s):
                if len(s) == n * 2:
                    res.append(s)
                    return 

                if left < n:
                    dfs(left + 1, right, s + '(')

                if right < left:
                    dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res

sol = Solution()
print(sol.generateParenthesis(n = 3))
print(sol.generateParenthesis(n = 1))
print(sol.generateParenthesis(n = 0))
print(sol.generateParenthesis(n = 4))


# Solution by using stack and backtracking 
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(open, closed):
            if open == closed == n:
                res.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()
            if closed < open:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return res

sol = Solution()
print(sol.generateParenthesis(n = 3))
print(sol.generateParenthesis(n = 1))
print(sol.generateParenthesis(n = 0))
print(sol.generateParenthesis(n = 4))
