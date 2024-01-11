class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        real_path = []
        for char in path:
            if real_path and char == '..':
                real_path.pop()
            elif char not in ['', '.', '..']:
                real_path.append(char)
        return '/' + '/'.join(real_path)

sol = Solution()
print(sol.simplifyPath(path = "/home/"))
print(sol.simplifyPath(path = "/../"))
print(sol.simplifyPath(path = "/home//foo/"))
print(sol.simplifyPath(path = "/a/./b/../../c/"))
