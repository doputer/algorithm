class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        open = ["(", "{", "["]
        close = [")", "}", "]"]

        while s:
            i = s.pop(0)

            if not stack or i in open:
                stack.append(i)
            else:
                if stack[-1] == "(" and i == ")":
                    stack.pop()
                elif stack[-1] == "{" and i == "}":
                    stack.pop()
                elif stack[-1] == "[" and i == "]":
                    stack.pop()
                else:
                    return False

        return True if not stack else False
