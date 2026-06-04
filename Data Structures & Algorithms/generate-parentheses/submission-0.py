class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(openN,closeN):
            if openN==closeN==n:
                res.append("".join(stack))
                return
            if openN<n:
                stack.append('(')
                backtrack(openN+1,closeN)
                stack.pop()
            if closeN<openN:
                stack.append(')')
                backtrack(openN,closeN+1)
                stack.pop()
        backtrack(0,0)
        return res


        """

           n = 1
           left = 1, right = 1
           ( => l = 0, r = 1
           ()

           n = 2  left -> (  less left than right )

                         l = 2, r = 2
                        /
            ( l = 1, r = 2
            /               \ 
        (( l = 0, r = 2     () l = 1, r = 1
        /
    (()  l = 0, r = 1       ()( l = 0, r = 1
    /                       /
   (()) l = 0, r = 0      ()() l = 0, r = 0


                n = 3

    (
          l = 2, r = 3
             () => l = 2, r = 2  ()(())
((  l = 1, r = 3
         (())()
/     
(((
/
((()
/
((())
/
((())) 




        """
        