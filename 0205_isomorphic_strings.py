class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_index, t_index = [], []
        for i in s:
            s_index.append(s.index(i))
        for i in t:
            t_index.append(t.index(i))

        return s_index == t_index
    
solution = Solution()
print(solution.isIsomorphic(s = "egg", t = "add"))
print(solution.isIsomorphic(s = "foo", t = "bar"))
print(solution.isIsomorphic(s = "paper", t = "title"))
print(solution.isIsomorphic(s = "bbbaaaba", t = "aaabbbba"))
