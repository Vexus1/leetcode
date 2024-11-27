# by bit manipulation
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n+1)
        for i in range(1, n+1):
            ans[i] = ans[i>>1] + (i&1)
        return ans
            
print(Solution().countBits(n = 5))
print(Solution().countBits(n = 2))

# by dynamic programing
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset*2 == i:
                offset *= 2
            ans[i] = ans[i-offset] + 1
        return ans
    
print(Solution().countBits(n = 5))
print(Solution().countBits(n = 2))
