class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            if i+1<len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"):
                dp[i]+=dp[i+2]
        return dp[0]
        """
        1234
        dp = {

            1: 3
            2: 2
            3: 1
            4: 1 
        }}
        2
        1 2 3 4 -> A B C D
        12 3 4 -> L C D
        1 23 4 -> 1 X D

            1
            2
            3 
            4 -> 1

$0

        0   1   2   3   4
        3   2   1   1   1
        """