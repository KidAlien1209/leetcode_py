class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        stack = []
        map = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        for x in s:
            if x in map.keys():
                stack.append(map[x])
            elif stack != [] and x == stack.pop():
                continue
            else:
                return False
        return stack==[]
        
if __name__ == '__main__':
    s = '{[()]}'
    print(Solution().isValid(s))