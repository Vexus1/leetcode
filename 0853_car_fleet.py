import unittest

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]) == 3

    def test2(self):
        assert sol.carFleet(target = 10, position = [3], speed = [3]) == 1

    def test3(self):
        assert sol.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]) == 1


if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 3/3')
        