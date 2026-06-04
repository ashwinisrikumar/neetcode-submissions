class Solution:
    def isValid(self, s: str) -> bool:
        d = {']':'[',')':'(','}':'{'}
        stack = []
        for ele in s:
            if ele in d:
                if stack and stack[-1] == d[ele]:
                    stack.pop()
                else:
                    return False
            else:    
                stack.append(ele)
        return True if not stack else False