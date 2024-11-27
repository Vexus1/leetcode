import unittest

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j-1] == typed[j]:
                j += 1
            else:
                return False
        return i == len(name)   

sol = Solution()
class Test(unittest.TestCase):
    def test1(self):
        assert sol.isLongPressedName(name = "rick", typed = "kric") == False
        
    def test2(self):
        assert sol.isLongPressedName(name = "alex", typed = "aaleex") == True

    def test3(self):
        assert sol.isLongPressedName(name = "saeed", typed = "ssaaedd") == False

    def test4(self):
        assert sol.isLongPressedName(name = "alex", typed = "aaleexa") == False

    def test5(self):
        assert sol.isLongPressedName(name = "alexd", typed = "ale") == False


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("passed 5/5")
