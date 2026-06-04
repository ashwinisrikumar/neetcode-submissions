class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s1 = []
        for char in tokens:
            if char == '+':
                s1.append(s1.pop()+s1.pop())
            elif char == '*':
                s1.append(s1.pop()*s1.pop())
            elif char == '-':
                c1,c2 = s1.pop(),s1.pop()
                s1.append(c2-c1)
            elif char == '/':
                c1,c2 = s1.pop(),s1.pop()
                s1.append(int(c2/c1))
            else:
                s1.append(int(char))
        return s1.pop()
        
        