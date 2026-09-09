class Solution:
    def isValid(self, s: str) -> bool:
        pars = {'}': '{', ')': '(', ']': '['}
        stack = list()
        for par in s:
            if par in pars:
                if stack and pars[par] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        return stack == []