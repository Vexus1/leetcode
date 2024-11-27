import unittest
from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        left = 0
        right = len(t) - 1
        q = deque(s)
        while left <= right:
            if not q:
                return True
            if t[left] == q[0]:
                q.popleft()
                left += 1
                continue
            elif t[right] == q[len(q) - 1]:
                q.pop()
                right -= 1
                continue
            left += 1
            right -= 1
        if not q:
            return True
        return False


sol = Solution()
class Test(unittest.TestCase):
    def test1(self) -> None:
        assert sol.isSubsequence(s = "abc", t = "ahbgdc") == True

    def test2(self) -> None:
        assert sol.isSubsequence(s = "axc", t = "ahbgdc") == False

    def test3(self) -> None:
        assert sol.isSubsequence(s = "", t = "") == True

    def test4(self) -> None:
        assert sol.isSubsequence(s = "b", t = "abc") == True


if __name__ == '__main__':
    unittest.main(verbosity=2)
