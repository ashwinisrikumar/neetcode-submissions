class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen=0
        resIndx=0
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    resLen=r-l+1
                    resIndx=l
                l=l-1
                r=r+1
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    resLen=r-l+1
                    resIndx=l
                l=l-1
                r=r+1
        return s[resIndx:resIndx+resLen]
        