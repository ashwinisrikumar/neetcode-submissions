class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIndx = 0
        resLen = 0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)>resLen:
                    resIndx = l
                    resLen = r-l+1
                l=l-1
                r=r+1            
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    resIndx = l
                    resLen=r-l+1
                l=l-1
                r=r+1
        return s[resIndx:resIndx+resLen]
        """
        ababd

        a -> left, right
        b -> a, a -> aba
        a -> b, b -> bab
            a, d
        b -> a,d
        d -> b 
babd
        aba -> 3 0,2

        bab -> 3, 0, 2

        a

        """
        