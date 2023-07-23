class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm"))
        result = []
        for word in words:
            for row in rows:
                if set(word.lower()).issubset(row):
                    result.append(word) 
        return result

sol = Solution()
print(sol.findWords(words = ["Hello","Alaska","Dad","Peace"]))
print(sol.findWords(words = ["omk"]))
print(sol.findWords(words = ["adsdf","sfd"]))
