class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l=0
        res = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1,l)
            mp[s[r]] = r
            res = max(res,r-l+1)
            """
                In this sliding window approach, 
                r - l + 1 calculates the total number of characters currently inside your "window"
                """
        return res

        
        