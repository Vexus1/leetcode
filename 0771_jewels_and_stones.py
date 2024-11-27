class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        jewels = list(jewels)
        for stone in stones:
            if stone in jewels:
                result += 1
        return result
    
solution = Solution()
print(solution.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(solution.numJewelsInStones(jewels = "z", stones = "ZZ"))