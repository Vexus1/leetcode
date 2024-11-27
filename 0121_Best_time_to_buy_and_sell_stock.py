import unittest

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            profit = max(profit, price - min_price)
            min_price = min(min_price, price)
        return profit

sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.maxProfit(prices = [7,1,5,3,6,4]) == 5

    def test2(self):
        assert sol.maxProfit(prices = [7,6,4,3,1]) == 0

    def test3(self):
        assert sol.maxProfit(prices = [1,2]) == 1


if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 3/3')
