import unittest

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        a = nums[0]
        result = []
        temp = [a]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                if len(temp) > 1:
                    result.append(f"{a}->{nums[i-1]}")
                else:
                    result.append(f"{nums[i-1]}")
                temp = []
                a = nums[i]
            temp.append(nums[i])
        if len(temp) > 1:
            result.append(f"{a}->{nums[-1]}")
        else:
            result.append(f"{nums[-1]}")
        return result


sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.summaryRanges(nums = [0,1,2,4,5,7]) == ['0->2', '4->5', '7']

    def test2(self):
        assert sol.summaryRanges(nums = [0,1]) == ['0->1']

    def test3(self):
        assert sol.summaryRanges(nums = [0,1,2,4,5,7]) == ['0->2', '4->5', '7']

    def test4(self):
        assert sol.summaryRanges(nums = [1,2]) == ['1->2']

    def test5(self):
        assert sol.summaryRanges(nums = [0,2,3,4,6,8,9]) == ['0', '2->4', '6', '8->9']

    def test6(self):
        assert sol.summaryRanges(nums = []) == []

if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('passed 6/6')
